from flask import Flask, request, render_template, send_from_directory
import os
import cv2
import torch
import numpy as np
import timm
from scipy.spatial import distance
import dlib

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"
app.config["PROCESSED_FOLDER"] = "static/processed"

# Ensure directories exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
os.makedirs(app.config["PROCESSED_FOLDER"], exist_ok=True)

# Load Haar Cascade for Face Detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Load Dlib Face Detector and Shape Predictor for Landmark Detection
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Load the Xception Model for Spoof Detection
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = timm.create_model("legacy_xception", pretrained=False, num_classes=2)
model.load_state_dict(torch.load("best_weighted_xception.pth", map_location=device))
model.to(device)
model.eval()

# Allowed file extensions
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "mp4", "avi", "mov"}

def allowed_file(filename):
    """Check if uploaded file has a valid extension."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# Eye Aspect Ratio Calculation
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

# Mouth Aspect Ratio Calculation
def mouth_aspect_ratio(mouth):
    A = distance.euclidean(mouth[2], mouth[10])
    B = distance.euclidean(mouth[4], mouth[8])
    C = distance.euclidean(mouth[0], mouth[6])
    return (A + B) / (2.0 * C)

# Process Image: Face Detection + Spoof Detection
def process_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        return None, "No Face Detected"

    fake_count = 0
    real_count = 0

    for (x, y, w, h) in faces:
        face = image[y:y+h, x:x+w]

        # Preprocess for Xception Model
        face_resized = cv2.resize(face, (224, 224))
        face_norm = face_resized.astype(np.float32) / 255.0
        face_tensor = torch.from_numpy(face_norm).permute(2, 0, 1).unsqueeze(0).to(device)

        with torch.no_grad():
            output = model(face_tensor)
            label = "Real" if output.argmax().item() == 1 else "Fake"

        if label == "Fake":
            fake_count += 1
        else:
            real_count += 1

    final_label = "Fake" if fake_count > real_count else "Real"

    # Draw bounding box and label
    color = (0, 255, 0) if final_label == "Real" else (0, 0, 255)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), color, 2)
        cv2.putText(image, final_label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    processed_image_path = os.path.join(app.config["PROCESSED_FOLDER"], "processed_image.jpg")
    cv2.imwrite(processed_image_path, image)

    return "processed/processed_image.jpg", final_label

# Process Video: Average Prediction & Display Single Frame
def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    fake_count = 0
    real_count = 0
    final_frame = None

    while True:
        success, frame = cap.read()
        if not success:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        for face in faces:
            shape = predictor(gray, face)
            shape_np = np.array([[p.x, p.y] for p in shape.parts()])

            if len(shape_np) < 68:
                continue  

            left_eye = shape_np[36:42]
            right_eye = shape_np[42:48]
            mouth = shape_np[48:68]

            if len(mouth) < 11:
                continue  

            ear = (eye_aspect_ratio(left_eye) + eye_aspect_ratio(right_eye)) / 2.0
            mar = mouth_aspect_ratio(mouth)

            EAR_THRESHOLD = 0.2
            MAR_THRESHOLD = 0.5

            label = "Real" if ear < EAR_THRESHOLD and mar > MAR_THRESHOLD else "Fake"

            if label == "Fake":
                fake_count += 1
            else:
                real_count += 1

            frame_count += 1
            final_frame = frame  # Store last processed frame

    cap.release()

    if frame_count == 0:
        return None, "No Face Detected"

    final_label = "Fake" if fake_count > real_count else "Real"

    if final_frame is not None:
        color = (0, 255, 0) if final_label == "Real" else (0, 0, 255)
        cv2.putText(final_frame, final_label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        processed_video_frame_path = os.path.join(app.config["PROCESSED_FOLDER"], "processed_video_frame.jpg")
        cv2.imwrite(processed_video_frame_path, final_frame)
        return "processed/processed_video_frame.jpg", final_label

    return None, final_label

# Flask Routes
@app.route("/", methods=["GET", "POST"])
def index():
    processed_image = None
    label = None

    if request.method == "POST":
        if "file" not in request.files:
            return "No file uploaded", 400

        file = request.files["file"]
        if file.filename == "":
            return "No selected file", 400

        if not allowed_file(file.filename):
            return render_template("index.html", label="Error: Unsupported file format. Please upload JPG, JPEG, PNG, MP4, AVI, or MOV.")

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        if file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            processed_image, label = process_image(filepath)
        elif file.filename.lower().endswith(('.mp4', '.avi', '.mov')):
            processed_image, label = process_video(filepath)

    return render_template("index.html", output_image=processed_image, label=label)

@app.route("/processed/<filename>")
def processed_file(filename):
    return send_from_directory(app.config["PROCESSED_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True)
