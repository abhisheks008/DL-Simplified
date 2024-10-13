import cv2
import dlib
import numpy as np
from imutils import face_utils
from scipy.spatial import distance as dist
import time

# Parameters for Blink Detection
EYE_AR_THRESH = 0.23  # Eye Aspect Ratio threshold
EYE_AR_CONSEC_FRAMES = 1  # Consecutive frames below threshold

# Load Haar Cascade Classifiers
frontal_face_cascade = cv2.CascadeClassifier('dataset/haarcascade_frontalface_default.xml')
profile_face_cascade = cv2.CascadeClassifier('dataset/haarcascade_profileface.xml')

# Load Dlib shape predictor for eye landmarks
predictor_path = "dataset/shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_path)

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

def detect_blink(frame, rect):
    shape = predictor(frame, rect)
    shape_np = face_utils.shape_to_np(shape)  # Convert shape to NumPy array

    left_eye = shape_np[36:42]  # Left eye landmarks
    right_eye = shape_np[42:48]  # Right eye landmarks

    left_EAR = eye_aspect_ratio(left_eye)
    right_EAR = eye_aspect_ratio(right_eye)

    ear = (left_EAR + right_EAR) / 2.0
    return ear

def main():
    cap = cv2.VideoCapture(0)
    COUNTER = 0
    TOTAL = 0

    # Instructions for the user
    instructions = [
        "Turn your head left and blink.",
        "Turn your head right and blink."
    ]

    for instruction in instructions:
        print(instruction)  # Print instruction for debugging
        time.sleep(2)  # Wait for 2 seconds before capturing

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Profile detection
            faces = frontal_face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
            profiles = profile_face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            # Blink detection
            for (x, y, w, h) in faces:
                rect = dlib.rectangle(x, y, x + w, y + h)
                ear = detect_blink(gray, rect)

                # Check for blink
                if ear < EYE_AR_THRESH:
                    COUNTER += 1
                else:
                    if COUNTER >= EYE_AR_CONSEC_FRAMES:
                        TOTAL += 1
                    COUNTER = 0

                # Draw rectangle around face
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            for (x, y, w, h) in profiles:
                # Draw rectangle around profile face
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Show blink count on frame
            cv2.putText(frame, f"Blinks: {TOTAL}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, instruction, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

            cv2.imshow("Liveness Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # Check if the user has blinked after instruction
            if TOTAL > 0:  # If at least one blink has been detected
                break

    # Check conditions for liveness
    if TOTAL > 0:
        print("Liveness Successful!")
        cv2.putText(frame, "Liveness Successful!", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        print("Liveness Failed!")
        cv2.putText(frame, "Liveness Failed!", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Liveness Detection", frame)
    cv2.waitKey(2000)  # Display the result for 2 seconds

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
