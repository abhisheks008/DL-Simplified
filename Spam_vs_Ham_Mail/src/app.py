import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

features = pickle.load(open('./features.pkl', 'rb'))
model = pickle.load(open('./XGBModel.pkl', 'rb'))
scaler = MinMaxScaler()

df = pd.DataFrame(columns=features)
df = df.drop('Prediction', axis=1)

df.loc[0] = 0

st.set_page_config(page_title='Spam Mail Detector')
st.title('Spam Vs Ham Mail Detector')

st.write('Enter the Content of the Mail')
mail = st.text_input(label='')

words = mail.split()
for word in words:
    if word in df.columns:
        df[word] += 1

if st.button('Submit'):

    X = scaler.fit_transform(df)
    pred = model.predict(X)
    if pred == 1:
        st.write('Spam Mail')
    else:
        st.balloons()
        st.write('Not Spam')

