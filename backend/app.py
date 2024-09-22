from flask import Flask, request, jsonify
from flask_cors import CORS
from test_model import test_model

app = Flask(__name__)
CORS(app)

@app.route('/')
def health_check():
    return "Server is running", 200

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    sex = data['sex']
    age = data['age']
    height_inches = data['height']
    weight_pounds = data['weight']
    
    # Call the test_model function
    prediction = test_model(sex, age, height_inches, weight_pounds)
    
    return jsonify({'predicted_event': prediction})

if __name__ == '__main__':
    app.run(debug=True)
