# Bank Customer Churn Prediction

This project focuses on predicting whether a bank customer is likely to leave (churn) or continue using the bank's services. Instead of relying on a single model, I experimented with four different deep learning architectures and compared their performance on the same dataset. To make the project more practical, I also developed a Streamlit web application that allows users to test the models through an interactive interface.

---

## What This Project Does

Customer churn is an important problem in the banking industry because retaining existing customers is often more cost-effective than acquiring new ones. The goal of this project is to identify customers who are at risk of leaving based on their demographic and financial information.

Given customer details such as age, balance, location, credit score, and account activity, the models generate a probability of churn. Predictions from all four models can be viewed individually, and an ensemble average is used to provide an overall assessment.

---

## Models Used

| Model                        | Purpose                                                                             |
| ---------------------------- | ----------------------------------------------------------------------------------- |
| **ANN**                      | A standard feedforward neural network used as the baseline model                    |
| **TabNet**                   | An attention-based architecture designed specifically for tabular data              |
| **FT-Transformer**           | A Transformer-based model that captures feature interactions through self-attention |
| **Autoencoder + Classifier** | Uses compressed feature representations before performing classification            |

All models were implemented using TensorFlow and Keras to maintain a consistent training and deployment workflow.

---

## Project Structure

```text
BankChurnPrediction/
│
├── Dataset/
│   ├── churn_modelling.csv
│   └── README.md
│
├── Images/
│   ├── img1.png
│   ├── img1_distributions.png
│   ├── img1_correlation.png
│   ├── img1_categorical.png
│   ├── img2_ann_training.png
│   ├── img2_shap.png
│   ├── img3_comparison.png
│   └── img4_roc_all.png
│
├── Model/
│   ├── bank_churn_prediction.ipynb
│   ├── README.md
│   └── saved_models/
│       ├── ann_model.h5
│       ├── autoencoder_model.h5
│       ├── encoder_model.h5
│       ├── ae_classifier.h5
│       ├── tabnet_weights.pkl
│       ├── ft_weights.pkl
│       ├── scaler.pkl
│       ├── input_dim.pkl
│       ├── feature_names.pkl
│       └── model_results.csv
│
├── Web App/
│   ├── web_app.py
│   ├── README.md
│   └── web_app.mp4
│
├── README.md
└── requirements.txt
```

---

## Dataset

The project uses the **Churn Modelling Dataset** available on Kaggle. It contains information about 10,000 bank customers and includes demographic, financial, and account-related features.

Dataset Link:
https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling

After downloading the dataset, rename the file to `churn_modelling.csv` and place it inside the `Dataset/` directory.

### Features Used

* CreditScore
* Geography
* Gender
* Age
* Tenure
* Balance
* NumOfProducts
* HasCrCard
* IsActiveMember
* EstimatedSalary

### Target Variable

* `Exited = 1` → Customer left the bank
* `Exited = 0` → Customer stayed with the bank

The dataset contains an imbalance between churned and retained customers, so SMOTE is used during training to improve class representation.

---

## How to Run

### Step 1: Clone or Download the Project

Download the project and ensure the folder structure remains unchanged.

### Step 2: Create the Environment

```bash
conda create -n tf python=3.9
conda activate tf
pip install -r requirements.txt
```

### Step 3: Add the Dataset

Place `churn_modelling.csv` inside the `Dataset/` folder.

### Step 4: Train the Models

Open the notebook located at:

```text
Model/bank_churn_prediction.ipynb
```

Run all cells from top to bottom.

The notebook will:

* Perform exploratory data analysis
* Generate visualizations
* Preprocess and scale the data
* Handle class imbalance using SMOTE
* Train all four models
* Perform hyperparameter tuning
* Generate SHAP explanations
* Save trained models and evaluation results

Depending on your hardware, training typically takes between 5 and 15 minutes.

### Step 5: Launch the Web Application

```bash
conda activate tf
cd "Web App"
streamlit run web_app.py
```

After launching, open:

```text
http://localhost:8501
```

in your browser.

---

## Evaluation

The primary evaluation metric used in this project is **ROC-AUC**, as it provides a better measure of model performance on imbalanced datasets than accuracy alone.

Additional metrics include:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

Particular attention is given to recall, since failing to identify a customer who is likely to churn can be more costly than incorrectly flagging a customer as high risk.

To improve interpretability, SHAP is used to identify the features that contribute most to model predictions.

---

## Additional Techniques Used

* **SMOTE** for handling class imbalance
* **Early Stopping** to reduce overfitting
* **ReduceLROnPlateau** for adaptive learning rate scheduling
* **Keras Tuner** for ANN hyperparameter optimization
* **SHAP** for explainable AI and feature importance analysis
* **Streamlit** for deployment and interactive predictions

---

## Tech Stack

* Python 3.9
* TensorFlow / Keras
* Scikit-Learn
* Imbalanced-Learn
* SHAP
* Keras Tuner
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit

---

## Results

| Model                    | ROC-AUC | Accuracy |
| ------------------------ | ------- | -------- |
| FT-Transformer           | ~0.87   | ~0.86    |
| TabNet                   | ~0.86   | ~0.85    |
| ANN                      | ~0.85   | ~0.86    |
| Autoencoder + Classifier | ~0.83   | ~0.84    |

The exact values may vary slightly between runs because of random initialization and data sampling techniques such as SMOTE.

---

## Final Thoughts

This project was developed to explore how different deep learning architectures perform on tabular data. It provided an opportunity to work with modern approaches such as TabNet and FT-Transformer while also comparing them against more traditional neural network models. Beyond model development, the project also covers explainability, hyperparameter tuning, and deployment, making it a complete end-to-end machine learning workflow.
