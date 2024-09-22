from flask import Flask, request, jsonify
from flask_cors import CORS
from test_model import test_model

app = Flask(__name__)
# Allow CORS for specific frontend URL
cors = CORS(app, resources={r"/predict": {"origins": "https://olympic-me-frontend-4zbehdbai-elephant333s-projects.vercel.app"}})

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
