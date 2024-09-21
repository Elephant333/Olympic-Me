from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # Import CORS
from test_model import test_model

app = Flask(__name__, static_folder='../frontend/build', static_url_path='')
CORS(app)  # Enable CORS for all routes

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

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
