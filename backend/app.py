from flask import Flask, request, jsonify
from flask_cors import CORS
from test_model import test_model
import logging

logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    logger.debug("Received request: %s", request.get_json())
    data = request.get_json()
    sex = data['sex']
    age = data['age']
    height_inches = data['height']
    weight_pounds = data['weight']
    
    # Log the extracted data
    logger.debug("Parsed data - Sex: %s, Age: %d, Height: %d, Weight: %d", sex, age, height_inches, weight_pounds)
    
    # Call the test_model function
    try:
        prediction = test_model(sex, age, height_inches, weight_pounds)
        logger.debug("Prediction made: %s", prediction)
        return jsonify({'predicted_event': prediction})
    except Exception as e:
        logger.error("Error occurred during prediction: %s", str(e))
        return jsonify({'error': 'Internal Server Error'}), 500

@app.errorhandler(Exception)
def handle_exception(e):
    logger.error("Unhandled exception: %s", str(e))
    return jsonify({"error": "Internal Server Error"}), 500

@app.after_request
def after_request(response):
    logger.debug("CORS headers set: %s", response.headers)
    return response

if __name__ == '__main__':
    app.run(debug=True)
