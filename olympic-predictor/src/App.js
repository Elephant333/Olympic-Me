import React, { useState } from "react";
import axios from "axios";
import { TextField, Button, Typography, Container } from "@mui/material";

function App() {
  const [sex, setSex] = useState("");
  const [age, setAge] = useState("");
  const [height, setHeight] = useState("");
  const [weight, setWeight] = useState("");
  const [predictedEvent, setPredictedEvent] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("/api/predict", {
        sex,
        age: parseInt(age),
        height: parseFloat(height),
        weight: parseFloat(weight),
      });
      setPredictedEvent(response.data.predicted_event);
    } catch (error) {
      console.error("Error predicting event:", error);
    }
  };

  return (
    <Container className="mt-10 p-6 border rounded-lg shadow-lg flex flex-col space-y-6" maxWidth="sm">
      <Typography variant="h4" align="center" gutterBottom>
        🏃Your Olympic Path🏋️
      </Typography>
      <form onSubmit={handleSubmit} className="flex flex-col space-y-6">
        {" "}
        {/* Added space-y-6 for vertical spacing */}
        <TextField
          label="Sex (M/F)"
          value={sex}
          onChange={(e) => setSex(e.target.value)}
          required
        />
        <TextField
          label="Age"
          type="number"
          value={age}
          onChange={(e) => setAge(e.target.value)}
          required
        />
        <TextField
          label="Height (inches)"
          type="number"
          value={height}
          onChange={(e) => setHeight(e.target.value)}
          required
        />
        <TextField
          label="Weight (pounds)"
          type="number"
          value={weight}
          onChange={(e) => setWeight(e.target.value)}
          required
        />
        <Button variant="contained" color="primary" type="submit">
          Predict Event
        </Button>
      </form>
      {predictedEvent && (
        <Typography
          variant="h5"
          align="center"
          className="mt-6 text-green-600 space-y-6"
        >
          You'd Be Best At: {predictedEvent}!
        </Typography>
      )}
    </Container>
  );
}

export default App;
