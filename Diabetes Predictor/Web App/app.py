import streamlit as st 
import pandas as pd  
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, SimpleRNN, LSTM
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras import models

# Load the dataset
df = pd.read_csv('Dataset/diabetes.csv')

# Set the title of the Streamlit app
st.title('Diabetes Predictor')

# Split the dataset into features (X) and target variable (y)
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Standardize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create two columns for layout using st.columns()
col1, col2 = st.columns(2)

# Function to get user input data
def get_user_data():
    with col1:
        st.header("Data")
        pg = st.slider('Pregnancies', 0, 17, 1)
        glucose = st.slider('Glucose', 0, 300, 120)
        bp = st.slider('Blood Pressure (Systolic Pressure)', 60, 180, 120)
        skin = st.slider('Skin Thickness in mm', 0, 100, 20)
        insulin = st.slider('Insulin', 0, 850, 80)
        bmi = st.slider('BMI (W (in kg)/ Height (in m)^2 )', 0, 80, 24)
        heritability = st.slider('Diabetes Pedigree Function', 0.0, 3.0, 0.4)
        age = st.slider('Age', 21, 90, 21)

        user_data = {
            'Pregnancies': pg, 
            'Glucose': glucose,
            'BloodPressure': bp,
            'SkinThickness' : skin,
            'Insulin': insulin,
            'BMI': bmi,
            'DiabetesPedigreeFunction': heritability,
            'Age': age
        }
        
        report_data = pd.DataFrame(user_data, index=[0])
        return report_data 

# Get user input data
user_data = get_user_data()

# Transpose the DataFrame for better display
user_df = pd.DataFrame(user_data)
user_df_transposed = user_df.transpose()  
user_df_transposed.columns = ['Value']  

# Scale the user input data
user_scaled = scaler.transform(user_df)

# Load the pre-trained model
model = models.load_model('Models/ann_model.h5')

# Make predictions using the model
prediction = model.predict(user_scaled)

# Display user data and prediction results
with col2:
    st.subheader("Patient Data")
    st.table(user_df_transposed)
    st.subheader("Your Report")
    if prediction[0] <= 0.5:
        st.success("You are healthy")
    else:
        st.warning("You are Diabetic")
