# This Streamlit App is for the Machine Learning model.


import streamlit as st
from nltk.stem import WordNetLemmatizer
import pickle
import nltk
import string
from nltk.corpus import stopwords

 
lemmatizer = WordNetLemmatizer()

# function of Data Preprocessing.
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(lemmatizer.lemmatize(i))
    
            
    return " ".join(y)


# Store the model in your file
# here we can store the tfidf and model pkl file in a specfic folder and use it.
tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('bnb.pkl','rb'))

st.title('SMS Spam Classification')

sms_input=st.text_area("Enter the text")

if st.button('Predict'):
    transform_sms=transform_text(sms_input)

    vector_input=tfidf.transform([transform_sms])

    result=model.predict(vector_input)[0]

    if result==1:
        st.title("SMS is Spam")

    else:
        st.title("SMS is not Spam")