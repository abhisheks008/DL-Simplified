# Artwork Image Recognition Webapp

## Goal 🎯

The primary objective of this project is to develop a user-friendly web application tailored for the seamless recognition of diverse artworks through advanced deep learning models.

## Model Used for the Web App 🧮

The web application utilizes a deep learning model trained for Artwork Image Classification. The model architecture includes the ResNet 152V2 pretrained model which is trained on the dataset of various artworks.

## Features of the Web App 🌐

- **Upload Artwork Image Recognition**: Allows users to upload various Artworks.
- **Prediction Display**: Provides predictions for type of Artworks based on the uploaded Artwork images.
- **Description about the artwork**: Provides Description about the artwork which has been predicted using Gemini AI API. 

**Note:** Ensure to update the paths accordingly based on your local machine's directory structure.

**Data and Model File Download:**

- Due to the large size of the dataset, it is not included in the GitHub repository. Please download the dataset from the provided location. 

- Similarly, the trained model file ('model.h5') is generated when you run the notebook successfully. Please keep this file in a directory named 'Web App' for smooth deployment without hiccups.

**Ensure to update the paths accordingly based on your local machine's directory structure**

### Project Directory Structure

```
Artwork Image Recognition
|- Dataset
  |- README.md
|- Images
  |- README.md
|- Model
  |- artwokrecognition-resnet152v2-97%.ipynb
  |- README.md
|- Web App
  |- app.py
  |- templates
    |- index.html
    |- layout.html
  |- static
    |- main.css
  |- model.h5
  |- README.md
|- requirements.txt
```
### Video Demonstration 🎥
[![]()](https://github.com/ArkaDutta-Maker/DL-Simplified/assets/52216225/a3799586-d42b-4a7d-956e-9cdb0c8bac23)

## How to Use

- **Requirements**: Ensure you have the necessary libraries and dependencies installed. You can find the list of required packages in the requirements.txt file.

- **Download Data**: Download the Artwork Image Recognition Dataset from Kaggle mentioned in the dataset section of the project.

- **Run the Jupyter Notebook**: Open the provided Jupyter Notebook file and run each cell sequentially. Make sure to update any file paths or configurations as needed for your environment.

- **Training and Evaluation**: Train the models using the provided data and evaluate their performance using metrics such as accuracy and loss.

- **Interpret Results**: Analyze the model's performance using the visualizations and metrics provided in the notebook.

### Signature ✒️

`Arka`

