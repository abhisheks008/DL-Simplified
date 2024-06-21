# Real Time Sudoku Solver

## 🎯 **Goal**
This project aims to develop an application that can solve standard Sudoku puzzles in real time using image processing and machine learning techniques, specifically Convolutional Neural Networks (CNN). The application captures video to identify the Sudoku board, solve the puzzle, and writes the solution on the board itself.

## 🧵 **Dataset**
The application starts by capturing video to identify the Sudoku board in real time. It processes the captured image to detect and recognize the numbers on the board, solves the puzzle, and overlays the solution back onto the original board.

If you want to try training the Convolution Network on your computer, you will need to download Chars74K Dataset http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/, takes images 1-9 (We only need 1-9) and put them in folders "1", "2", ..., "9" respectively in the same directory with where you put all my Python files. After that, just run digitRecognition.py

## 🧾 **Description**
This project leverages image processing and machine learning to create a real-time Sudoku solver. The core functionality involves using a Convolutional Neural Network (CNN) to recognize the digits on the Sudoku board from a live video feed. The recognized digits are then processed to solve the Sudoku puzzle, and the solution is displayed directly on the video feed. This application combines the power of computer vision and deep learning to deliver a seamless and interactive Sudoku-solving experience.

## 🧮 **What I had done!**
1. Video Capture and Preprocessing: Implemented video capture to continuously get frames from the webcam. Applied image preprocessing techniques to enhance the quality of the captured frames for better digit recognition.
2. Digit Recognition: Trained a Convolutional Neural Network (CNN) model to recognize digits from the preprocessed images. Integrated the trained model into the application to identify digits on the Sudoku board.
3. Sudoku Solver: Developed an algorithm to solve the Sudoku puzzle using the recognized digits. Ensured the solution is accurate and efficient.
4. Overlay Solution: Implemented a method to overlay the solved Sudoku puzzle back onto the original video feed, displaying the solution in real time.

   The step by step images are provided in the Images Folder.

## 📚 **Libraries Needed**
1. keras==2.3.1
2. numpy==1.22.0
3. opencv-python==4.2.0.34
4. scipy==1.4.1
5. import-ipynb==0.1.3

## **How To Start?**
`sudoku testing.ipynb` is the entry of the application. Just run the file and show the sudoku image as soon as the window opens. Make sure to have all the requirements.

## 📢 **Conclusion**
The real-time Sudoku solver successfully combines image processing and machine learning techniques to deliver an interactive and efficient solution for solving Sudoku puzzles. The application demonstrates high accuracy in digit recognition and puzzle-solving, thanks to the trained CNN model. 
By leveraging CNN for digit recognition and combining it with efficient puzzle-solving algorithms, the project provides a seamless user experience in solving Sudoku puzzles directly from a live video feed. The accuracy and efficiency of the solution make it a valuable tool for Sudoku enthusiasts and showcase the potential of integrating image processing and machine learning for real-time applications.

## Video Demonstration
![Real Time Sudoku Solver](https://github.com/abckhush/DL-Simplified/assets/127378920/6485b261-b624-46e5-8947-61c13390fe11)

## ✒️ **Your Signature**
Khushi Kalra <br>
<a href="https://www.github.com/abckhush">Github</a> <br>
<a href="https://www.linkedin.com/in/kalrakhushi/">LinkedIn</a>
