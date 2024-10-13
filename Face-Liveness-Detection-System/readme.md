# Face Liveness Detection System 👤💻

This project implements a Face Liveness Detection System using profile detection and blink detection techniques. The system is designed to verify whether a person is physically present during the authentication process by analyzing facial features and eye blinks. 🔍

## Methodology 🛠️

The system employs the following methodologies:

1. **Profile Detection** 📸:
   - The system utilizes Haar Cascade classifiers to detect frontal and profile faces. This helps in determining whether the user is facing the camera properly.
   - The classifiers are loaded from XML files that contain pre-trained models.

2. **Blink Detection** 👁️:
   - Dlib's shape predictor is used to detect eye landmarks, allowing the calculation of the Eye Aspect Ratio (EAR).
   - If the EAR falls below a certain threshold, the system counts it as a blink. The system requires a specific number of blinks to confirm that the user is alive.

3. **User Instructions** 🗣️:
   - The user is instructed to turn left or right and to blink their eyes as prompted.
   - If the conditions of turning and blinking are satisfied within the specified limits, the system declares the liveness detection as successful; otherwise, it fails.

## Requirements 📋

To run this project, ensure you have the following dependencies installed. You can install them using pip:

```bash
pip install -r requirements.txt
```

### Running the Main File ▶️

To run the main file and start the liveness detection process, follow these steps:

1. Make sure you have a working webcam connected to your computer. 📷
2. Navigate to the project directory in your terminal or command prompt.
3. Execute the following command:

   ```bash
   python main.py
   ```

4. Follow the on-screen instructions to complete the liveness detection process. 🏁

## File Structure 📂

```
your_project_directory/
│
├── dataset/
│   ├── haarcascade_frontalface_default.xml
│   ├── haarcascade_profileface.xml
│   └── shape_predictor_68_face_landmarks.dat
│
├── main.py
└── README.md
```

## Contributing 🤝

contributor:**Pratik Wayal**. Feel free to connect: [GitHub](https://github.com/pratikwayal01). All contributions are welcome! 🌟
```
