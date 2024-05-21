# Hand Navigation Landmark

Full Name : Utsab Samadder
email : utsab.samadder@gmail.com

**Project Approach**
1. Run the HandAnalysis.ipynb file in Google Colab
2. You will get a best.pt file which is actually the model trained.

Use this code and the best.pt file to do real time tests.

```python
from ultralytics import YOLO
import cv2
import math
import yaml

cap = cv2.VideoCapture(0)  # For Webcam
model = YOLO("best.pt")

# Load class names from data.yaml
with open("data.yaml", "r") as file:
    data = yaml.safe_load(file)
classNames = data['names']

# Print class names
print("Class Names:", classNames)

# Define colors for different classes
class_colors = {
    'Anticlockwise-dLyJ': (255, 0, 0),  # Blue
    'Backward': (0, 255, 0),        # Green
    'Clockwise': (0, 0, 255),       # Red
    'Down': (255, 255, 0),          # Cyan
    'Forward': (0, 255, 255),       # Yellow
    'Left': (255, 0, 255),          # Magenta
    'Right': (128, 128, 0),         # Olive
    'Up': (128, 0, 128),            # Purple
    'Wave': (0, 128, 128)           # Teal
}

while True:
    success, img = cap.read()
    if not success:
        break

    results = model(img, stream=True)
    for r in results:
        for box in r.boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1

            # Confidence
            conf = box.conf[0].item()
            # Class Name
            cls = int(box.cls[0])

            # Check if class index is within the range of classNames
            if 0 <= cls < len(classNames):
                current_class = classNames[cls]

                # Only draw if confidence is above threshold
                if conf > 0.50:
                    color = class_colors.get(current_class, (255, 255, 255))  # Default color is white
                    label = f'{current_class} {conf:.2f}'
                    cv2.putText(img, label, (x1, max(35, y1)), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                    cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
            else:
                print(f"Warning: Detected class ID {cls} not found in classNames list.")

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

```


*The python file has not been updated here because the repo was of more than 2gb size*