import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, KFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, accuracy_score
import matplotlib.pyplot as plt

# Load and preprocess data
data = pd.read_csv('Ground Water .csv')

# Fill NaN values in numeric columns with median
numeric_columns = data.select_dtypes(include='number').columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].median())

# Handle outliers using quantile clipping
numeric_data = data.select_dtypes(include=[np.number])
data[numeric_data.columns] = numeric_data.clip(
    lower=numeric_data.quantile(0.01), 
    upper=numeric_data.quantile(0.99), 
    axis=1
)

# Convert categorical variables to dummy variables
data = pd.get_dummies(data)

# Scale the features
scaler = StandardScaler()
data[data.select_dtypes(include=['float64']).columns] = scaler.fit_transform(
    data.select_dtypes(include=['float64'])
)

# Drop specified columns and split features/target
data = data.drop(data.columns[[1, 2]], axis=1)
X = data.iloc[:,:-3]
y = data.iloc[:, -1]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Initialize Random Forest model
rf_model = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    n_jobs=-1
)

# Perform K-fold cross-validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)
mse_scores = []
accuracy_scores = []
rmse_scores = []

for fold, (train_index, val_index) in enumerate(kf.split(X_train), 1):
    # Split data for this fold
    X_train_fold = X_train.iloc[train_index]
    X_val_fold = X_train.iloc[val_index]
    y_train_fold = y_train.iloc[train_index]
    y_val_fold = y_train.iloc[val_index]
    
    # Train the model
    rf_model.fit(X_train_fold, y_train_fold)
    
    # Make predictions
    y_pred = rf_model.predict(X_val_fold)
    
    # Calculate metrics
    mse = mean_squared_error(y_val_fold, y_pred)
    rmse = np.sqrt(mse)
    
    # Convert predictions to binary for accuracy calculation
    y_pred_binary = (y_pred >= 0.5).astype(int)
    y_val_binary = (y_val_fold >= 0.5).astype(int)
    acc = accuracy_score(y_val_binary, y_pred_binary) * 100
    
    # Store scores
    mse_scores.append(mse)
    accuracy_scores.append(acc)
    rmse_scores.append(rmse)
    
    print(f"\nFold {fold}:")
    print(f"MSE: {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"Accuracy: {acc:.2f}%")

# Calculate and print average metrics
avg_mse = np.mean(mse_scores)
avg_rmse = np.mean(rmse_scores)
avg_accuracy = np.mean(accuracy_scores)

print("\nAverage Metrics across all folds:")
print(f"Average MSE: {avg_mse:.4f}")
print(f"Average RMSE: {avg_rmse:.4f}")

# Plot the metrics
plt.figure(figsize=(15, 5))

# Plot Accuracy
plt.subplot(1, 3, 1)
plt.plot(range(1, 6), accuracy_scores, marker='o')
plt.title('Accuracy across Folds')
plt.xlabel('Fold')
plt.ylabel('Accuracy (%)')

# Plot MSE
plt.subplot(1, 3, 2)
plt.plot(range(1, 6), mse_scores, marker='o', color='red')
plt.title('MSE across Folds')
plt.xlabel('Fold')
plt.ylabel('MSE')

# Plot RMSE
plt.subplot(1, 3, 3)
plt.plot(range(1, 6), rmse_scores, marker='o', color='green')
plt.title('RMSE across Folds')
plt.xlabel('Fold')
plt.ylabel('RMSE')

plt.tight_layout()
plt.show()

# Feature Importance Analysis
feature_importance = pd.DataFrame({
    'feature': X_train.columns,
    'importance': rf_model.feature_importances_
})
feature_importance = feature_importance.sort_values('importance', ascending=False)

# Plot feature importance
plt.figure(figsize=(10, 6))
plt.bar(range(len(feature_importance)), feature_importance['importance'])
plt.xticks(range(len(feature_importance)), feature_importance['feature'], rotation=45, ha='right')
plt.title('Feature Importance in Random Forest Model')
plt.tight_layout()
plt.show()
