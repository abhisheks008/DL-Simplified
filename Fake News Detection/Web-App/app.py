from flask import Flask, render_template, request, jsonify,redirect
import nltk
from nltk.corpus import stopwords
import re
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import tensorflow as tf
import csv

app = Flask(__name__)
ps = PorterStemmer()
nltk.download('stopwords')


model = tf.keras.models.load_model('/Users/pushpakreddy/Downloads/Fake-News/model.h5')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

def predict(text):
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    vectorizer = TfidfVectorizer()
    vectorizer.fit([review]) 
    review_vect = vectorizer.transform([review])
    prediction = 'FAKE' if model.predict(review_vect) == 0 else 'REAL'
    return prediction
    

@app.route('/', methods=['POST'])
def webapp():
    text = request.form['text']
    prediction = predict(text)
    return render_template('index.html', text=text, result=prediction)

@app.route('/predict/', methods=['GET','POST'])
def api():
    text = request.args.get("text")
    prediction = predict(text)
    return jsonify(prediction=prediction)

@app.route('/feedback', methods=['POST'])
def handle_feedback():
  feedback = request.json['feedback']
  text = request.json['text']
  
  with open('feedback.csv', mode='a', newline='') as feedback_file:
    feedback_writer = csv.writer(feedback_file)
    feedback_writer.writerow([text, int(feedback == 'real')])
  
  return redirect('/')

if __name__ == "__main__":
    app.run(debug=True,port=8080)  
