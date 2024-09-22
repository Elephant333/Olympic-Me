import numpy as np
import tensorflow as tf
import joblib
import itertools
import argparse

# Load the TensorFlow Lite model and encoder
interpreter = tf.lite.Interpreter(model_path='model.tflite')
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
encoder = joblib.load('encoder.pkl')

# Function to test the model with new biometric inputs
def test_model(sex, age, height_inches, weight_pounds):
    # Convert height to centimeters and weight to kilograms
    height_cm = height_inches * 2.54
    weight_kg = weight_pounds * 0.453592

    # Prepare input data using numpy for efficiency
    sex_value = 1 if sex == 'M' else 0
    input_data = np.array([[sex_value, age, height_cm, weight_kg]], dtype=np.float32)

    # Set input tensor
    interpreter.set_tensor(input_details[0]['index'], input_data)
    
    # Run inference
    interpreter.invoke()
    
    # Get prediction
    prediction = interpreter.get_tensor(output_details[0]['index'])
    
    # Get predicted event
    predicted_event = encoder.inverse_transform([prediction.argmax()])[0]
    
    return predicted_event

# Function to iterate through combinations of inputs
def iterate_combinations():
    sexes = ['M', 'F']
    ages = [18, 25, 30]  # Example ages
    heights = [60, 65, 70, 75]  # Example heights in inches
    weights = [120, 150, 180, 210]  # Example weights in pounds

    for sex, age, height, weight in itertools.product(sexes, ages, heights, weights):
        predicted_event = test_model(sex, age, height, weight)
        print(f"Sex: {sex}, Age: {age}, Height: {height} inches, Weight: {weight} pounds => Predicted Event: {predicted_event}")

# Function to get individual inputs and make predictions
def individual_input():
    while True:
        sex = input("Enter sex (M/F): ")
        age = int(input("Enter age: "))
        height = float(input("Enter height in inches: "))
        weight = float(input("Enter weight in pounds: "))
        
        predicted_event = test_model(sex, age, height, weight)
        print(f"Predicted Event: {predicted_event}")

        # Ask if the user wants to continue
        continue_input = input("Do you want to enter another set of inputs? (yes/no): ").strip().lower()
        if continue_input != 'yes':
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict Olympic events based on biometric data.")
    parser.add_argument('--mode', choices=['individual', 'iterate'], default='individual',
                        help="Choose 'individual' for single input or 'iterate' for combinations (default: individual).")

    args = parser.parse_args()

    if args.mode == 'individual':
        individual_input()
    elif args.mode == 'iterate':
        iterate_combinations()
