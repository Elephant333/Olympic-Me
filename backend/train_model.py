import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load and preprocess your data
data = pd.read_csv('athlete_events.csv')

# Dropping unnecessary columns
data = data[['Sex', 'Age', 'Height', 'Weight', 'Event']].dropna()

# Encoding categorical data
encoder = LabelEncoder()
data['Event'] = encoder.fit_transform(data['Event'])
data['Sex'] = data['Sex'].apply(lambda x: 1 if x == 'M' else 0)

# Splitting data
X = data[['Sex', 'Age', 'Height', 'Weight']]
y = data['Event']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Define a model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(len(encoder.classes_), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Save the model and the encoder
model.save('model.h5')
import joblib
joblib.dump(encoder, 'encoder.pkl')
