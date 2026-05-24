import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

from xgboost import XGBRegressor

import joblib

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("../Dataset/Bengaluru_House_Data.csv")

print(df.head())

print(df.info())

# -----------------------------
# Remove Unnecessary Columns
# -----------------------------

df = df.drop(['society', 'availability'], axis=1)

# -----------------------------
# Handle Missing Values
# -----------------------------

df = df.dropna()

# -----------------------------
# Convert total_sqft to numeric
# -----------------------------

def convert_sqft(x):
    try:
        return float(x)
    except:
        return None

df['total_sqft'] = df['total_sqft'].apply(convert_sqft)

df = df.dropna()

# -----------------------------
# Convert size column to numeric
# -----------------------------

df['bhk'] = df['size'].str.split().str[0]

df['bhk'] = pd.to_numeric(df['bhk'], errors='coerce')

# Drop original size column

df = df.drop('size', axis=1)

# -----------------------------
# Encode categorical columns
# -----------------------------

label_encoder = LabelEncoder()

categorical_columns = ['area_type', 'location']

for col in categorical_columns:
    df[col] = label_encoder.fit_transform(df[col])

# -----------------------------
# Correlation Heatmap
# -----------------------------

plt.figure(figsize=(10, 8))

sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

plt.title("Correlation Heatmap")

plt.savefig("../Images/heatmap.png")

plt.show()

# -----------------------------
# Price Distribution
# -----------------------------

plt.figure(figsize=(8, 5))

sns.histplot(df['price'], bins=30)

plt.title("Price Distribution")

plt.savefig("../Images/distribution.png")

plt.show()

# -----------------------------
# Feature Selection
# -----------------------------

X = df.drop('price', axis=1)

y = df['price']

# -----------------------------
# Train Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Linear Regression
# -----------------------------

lr_model = LinearRegression()

lr_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)

# -----------------------------
# Random Forest
# -----------------------------

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

# -----------------------------
# XGBoost
# -----------------------------

xgb_model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=6,
    random_state=42
)

xgb_model.fit(X_train, y_train)

xgb_pred = xgb_model.predict(X_test)

# -----------------------------
# Evaluation Function
# -----------------------------

def evaluate_model(name, y_test, predictions):

    mae = mean_absolute_error(y_test, predictions)

    mse = mean_squared_error(y_test, predictions)

    rmse = np.sqrt(mse)

    r2 = r2_score(y_test, predictions)

    print(f"\n{name} Results")

    print("MAE:", mae)

    print("MSE:", mse)

    print("RMSE:", rmse)

    print("R2 Score:", r2)

# -----------------------------
# Evaluate Models
# -----------------------------

evaluate_model("Linear Regression", y_test, lr_pred)

evaluate_model("Random Forest", y_test, rf_pred)

evaluate_model("XGBoost", y_test, xgb_pred)

# -----------------------------
# Save Best Model
# -----------------------------

joblib.dump(xgb_model, "model.pkl")

print("\nModel Saved Successfully!")

# -----------------------------
# Sample Prediction
# -----------------------------

sample_data = X_test.iloc[0:1]

prediction = xgb_model.predict(sample_data)

print("\nPredicted Price:", prediction[0])