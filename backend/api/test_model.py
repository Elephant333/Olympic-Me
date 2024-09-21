import pandas as pd
import tensorflow as tf
import joblib
import itertools
import argparse

# Load the model and encoder
model = tf.keras.models.load_model('../model.h5')
encoder = joblib.load('../encoder.pkl')

# Function to test the model with new biometric inputs
def test_model(sex, age, height_inches, weight_pounds):
    # Convert height to centimeters and weight to kilograms
    height_cm = height_inches * 2.54
    weight_kg = weight_pounds * 0.453592

    # Prepare input data
    input_data = pd.DataFrame([[1 if sex == 'M' else 0, age, height_cm, weight_kg]], columns=['Sex', 'Age', 'Height', 'Weight'])
    
    # Make prediction
    prediction = model.predict(input_data)
    
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
