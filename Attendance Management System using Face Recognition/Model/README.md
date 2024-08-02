# 🤖 Face Recognition in Deep Learning

## 📚 Models Used
1. **DeepFace**
2. **FaceNet**
3. **VGGNet**
4. **FaceRecognition Library**

### 🎯 Accuracy Comparison
- **FaceRecognition Library**: Provides higher accuracy as it does not require any models.
- **FaceNet and DeepFace**: Offer similar accuracy.
- **VGGNet**: Delivers lower accuracy.

## 📦 Required Packages
Install the following packages:
- `numpy`
- `keras`
- `deepface`
- `PIL`
- `tkinter`
- `cv2`
- `os`
- `tensorflow`
- `mtcnn`

Additionally, download and store the following in the same working folder:
1. `dlib-19.24.1-cp311-cp311-win_amd64.whl`
2. `facenet_keras.h5`
3. `vgg_face_weights.h5`

## 📁 Folder Structure
Create the following folders:
- `dataset` (store your own images for recognition and dataset purposes)
- `imagebasics`

## 📄 CSV File
Create an `Attendance.csv` file.

## 📝 Python Files
Create the following Python files and ensure to rename them as needed:
- When running `DeepFace.py`, rename `AttendenceProject.py` to `DeepFace.py` in `gui2.py` and `GUI.py`.

## 🚀 Running the Project
Run `gui2.py` to start the image recognition process.