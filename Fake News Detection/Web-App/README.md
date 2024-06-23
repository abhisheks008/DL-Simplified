# Fake News Predictor

This web app helps users determine the authenticity of news articles by leveraging machine learning models.

**Features:**

* Text input for entering news content
* Real-time prediction of "Real" or "Fake" based on a trained model
* Feedback can be provided by the users.

**Installation:**
1. Clone this repository: `git clone https://github.com/abhisheks008/DL-Simplified.git`
2. Create an environment for this project but create in this Fake news detection folder only.
3. Install all the packages mention in `app.py`. file.

**Usage:**
1. Run the app (`app.py`).
2. Enter a news article in the provided text area.
3. Click the "Predict" button.
4. View the predicted output (Real or Fake) and also give the feedback whether the model is giving proper predictions or not. 


**License:**
MIT License 

**Demonstration video!!**

https://github.com/AKing-283/DL-Simplified/assets/154039781/f45b5719-008a-4d38-ac6a-bbd6871a3892



**Folder Structure:**
1. Use saved model of H5 format as in `app.py` we have loaded the saved model's path of this format.
   If you want you can change the format according to your interest. 
2. In templates folder contains `index.html` which is the front end of this project.
3. A new seperate file(`feedback.csv`) will be created by the app.py which contains the feedbacks and 
   gets updated automatically when user will provide the feedback.
4. `app.py` is the main python program file which contains the program of flask . We will be getting output by running command:
  ```bash 
python3 app.py ```
