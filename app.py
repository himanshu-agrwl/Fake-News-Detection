from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np


model_path = 'model (1).pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
  
    news_text = request.form.get('URLs')

    features = vectorizer.transform([news_text])

    
   
    prediction = model.predict(features)[0]
    output = 'FAKE' if prediction == 1 else 'NOT FAKE'

    return render_template('index.html', prediction_text='Prediction: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)