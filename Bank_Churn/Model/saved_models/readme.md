# Model

This folder contains the main notebook used for training and evaluating all models, along with the saved model files required by the Streamlit web application.

---

## Folder Structure

```text
Model/
├── bank_churn_prediction.ipynb
├── README.md
│
├── saved_models/
│   ├── ann_model.h5
│   ├── autoencoder_model.h5
│   ├── encoder_model.h5
│   ├── ae_classifier.h5
│   ├── tabnet_weights.pkl
│   ├── ft_weights.pkl
│   ├── scaler.pkl
│   ├── input_dim.pkl
│   ├── feature_names.pkl
│   └── model_results.csv
│
└── kt_dir/
    └── churn_hp/
```

---

## Models Used

### ANN

The ANN serves as the baseline model for this project. It is a fully connected neural network with Batch Normalization and Dropout layers to improve generalization and reduce overfitting. Since it only uses standard Keras layers, it can be saved and loaded directly using the `.h5` format.

### TabNet

TabNet was implemented from scratch using TensorFlow. Unlike traditional neural networks, it uses an attention mechanism to focus on the most relevant features at different decision steps. Because it contains custom layers, only the model weights are saved and the architecture is rebuilt when loading the model.

### FT-Transformer

The FT-Transformer adapts the Transformer architecture for tabular data. Each feature is converted into a token representation, and self-attention is used to learn relationships between features. Similar to TabNet, only the weights are stored and the model is reconstructed when needed.

### Autoencoder + Classifier

This approach uses an autoencoder to learn compressed representations of customer data. The encoder output is then used as input to a separate classifier. Both the encoder and classifier are saved independently so they can be loaded and used sequentially during prediction.

---

## Running the Notebook

Open `bank_churn_prediction.ipynb` and run all cells from top to bottom. Before running the notebook, make sure the dataset is available in the Dataset folder.

The notebook will:

* Perform exploratory data analysis (EDA)
* Generate and save visualizations
* Preprocess the data
* Handle class imbalance using SMOTE
* Train all four models
* Perform hyperparameter tuning for the ANN
* Generate SHAP explanations
* Save trained models and evaluation results

Depending on your system, training may take several minutes. The hyperparameter tuning section generally takes the longest to complete.

---

## Model Saving

The ANN and Autoencoder models are saved using the standard Keras `.h5` format. For TabNet and FT-Transformer, only the model weights are saved because custom TensorFlow layers can sometimes create compatibility issues across different environments and TensorFlow versions.

When the web application starts, it rebuilds these architectures and loads the saved weights automatically.

---

## Evaluation

Performance may vary slightly between runs due to random initialization, train-test splitting, and SMOTE sampling. For model comparison, ROC-AUC is considered the primary evaluation metric since the dataset is not perfectly balanced.
