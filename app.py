from flask import Flask, request, jsonify
import pandas as pd
import tensorflow as tf
import joblib
from test_model import test_model

# Load the model and encoder
model = tf.keras.models.load_model('model.h5')
encoder = joblib.load('encoder.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    sex = data['sex']
    age = data['age']
    height_inches = data['height']
    weight_pounds = data['weight']
    
    # Call your test_model function here
    prediction = test_model(sex, age, height_inches, weight_pounds)
    
    return jsonify({'predicted_event': prediction})

if __name__ == '__main__':
    app.run(debug=True)
