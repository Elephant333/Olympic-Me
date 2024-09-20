import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [sex, setSex] = useState('');
    const [age, setAge] = useState('');
    const [height, setHeight] = useState('');
    const [weight, setWeight] = useState('');
    const [predictedEvent, setPredictedEvent] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:5000/predict', {
                sex,
                age: parseInt(age),
                height: parseFloat(height),
                weight: parseFloat(weight)
            });
            setPredictedEvent(response.data.predicted_event);
        } catch (error) {
            console.error('Error predicting event:', error);
        }
    };

    return (
        <div>
            <h1>Olympic Event Predictor</h1>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="Sex (M/F)" value={sex} onChange={(e) => setSex(e.target.value)} required />
                <input type="number" placeholder="Age" value={age} onChange={(e) => setAge(e.target.value)} required />
                <input type="number" placeholder="Height (inches)" value={height} onChange={(e) => setHeight(e.target.value)} required />
                <input type="number" placeholder="Weight (pounds)" value={weight} onChange={(e) => setWeight(e.target.value)} required />
                <button type="submit">Predict Event</button>
            </form>
            {predictedEvent && <h2>Predicted Event: {predictedEvent}</h2>}
        </div>
    );
}

export default App;
