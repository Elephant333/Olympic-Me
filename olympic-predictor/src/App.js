import React, { useState } from "react";
import axios from "axios";
import {
  TextField,
  Button,
  Typography,
  Container,
  CircularProgress,
  Box,
} from "@mui/material";

function App() {
  const [sex, setSex] = useState("");
  const [age, setAge] = useState("");
  const [feet, setFeet] = useState("");
  const [inches, setInches] = useState("");
  const [weight, setWeight] = useState("");
  const [predictedEvent, setPredictedEvent] = useState("");
  const [loading, setLoading] = useState(false);
  const [feetError, setFeetError] = useState("");
  const [inchesError, setInchesError] = useState("");
  const [ageError, setAgeError] = useState("");
  const [weightError, setWeightError] = useState("");
  const [sexError, setSexError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Clear previous error
    setFeetError("");
    setInchesError("");
    setAgeError("");
    setWeightError("");
    setSexError("");
    let isError = false;

    const totalHeightInInches = parseInt(feet) * 12 + parseFloat(inches);
    const ageValue = parseInt(age);
    const weightValue = parseFloat(weight);

    // Prevent submission if validation fails
    if (!["M", "F"].includes(sex)) {
      setSexError("Sex must be either M or F");
      isError = true;
    }
    if (parseInt(feet) <= 0) {
      setFeetError("Feet must be greater than 0");
      isError = true;
    }
    if (parseFloat(inches) < 0 || parseFloat(inches) > 12) {
      setInchesError("Inches must be between 0 and 12");
      isError = true;
    }
    if (ageValue <= 0) {
      setAgeError("Age must be greater than 0");
      isError = true;
    }
    if (ageValue > 125) {
      setAgeError("I don't believe you're that old, try again");
      isError = true;
    }
    if (weightValue <= 0) {
      setWeightError("Weight must be greater than 0");
      isError = true;
    }
    if (parseInt(feet) >= 9) {
      setFeetError("I don't believe you're that tall, try again");
      isError = true;
    }
    if (weightValue > 1500) {
      setWeightError("I don't believe you're that heavy, try again");
      isError = true;
    }
    if (isError) {
      return;
    }

    setLoading(true); // Set loading to true when starting the request
    try {
      // use http://localhost:5000/predict to test locally
      // https://olympic-me-backend.onrender.com/predict when backend on render
      const response = await axios.post("https://olympic-me-backend.onrender.com/predict", {
        sex,
        age: ageValue,
        height: totalHeightInInches,
        weight: weightValue,
      });
      setPredictedEvent(response.data.predicted_event);
    } catch (error) {
      console.error("Error predicting event:", error);
    } finally {
      setLoading(false); // Set loading to false when the request is done
    }
  };

  return (
    <Container
      className="mt-10 p-6 border rounded-lg shadow-lg flex flex-col space-y-6"
      maxWidth="sm"
    >
      <Typography variant="h4" align="center" gutterBottom>
        🏃Your Olympic Path🏋️
      </Typography>
      <form onSubmit={handleSubmit} className="flex flex-col space-y-6">
        <TextField
          label="Sex (M/F)"
          value={sex}
          onChange={(e) => setSex(e.target.value)}
          error={!!sexError}
          helperText={sexError}
          required
          className="w-full"
        />
        <TextField
          label="Age"
          type="number"
          value={age}
          onChange={(e) => setAge(e.target.value)}
          error={!!ageError}
          helperText={ageError}
          required
          className="w-full"
        />
        <Box display="flex" width="100%" className="space-x-2">
          <TextField
            label="Height (feet)"
            type="number"
            value={feet}
            onChange={(e) => setFeet(e.target.value)}
            error={!!feetError}
            helperText={feetError}
            required
            className="flex-1"
          />
          <TextField
            label="Height (inches)"
            type="number"
            value={inches}
            onChange={(e) => setInches(e.target.value)}
            error={!!inchesError}
            helperText={inchesError}
            required
            className="flex-1"
          />
        </Box>
        <TextField
          label="Weight (pounds)"
          type="number"
          value={weight}
          onChange={(e) => setWeight(e.target.value)}
          error={!!weightError}
          helperText={weightError}
          required
          className="w-full"
        />
        <Button
          variant="contained"
          color="primary"
          type="submit"
          disabled={loading}
          className="relative w-full"
        >
          {loading ? (
            <CircularProgress
              size={24}
              className="absolute left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-1/2"
            />
          ) : (
            "Predict Your Event"
          )}
        </Button>
      </form>
      {predictedEvent && (
        <Typography variant="h5" align="center" className="mt-6 text-green-600">
          You'd Be Best At: {predictedEvent}!
        </Typography>
      )}
      <footer className="mt-10 py-4 text-black text-center">
        <div className="text-sm">
          <p>Powered with Machine Learning</p>
          <p>
            Made by <a href="https://nathanjli.com" target="_blank" rel="noopener noreferrer" className="text-blue-500 underline">Nathan Li</a>
          </p>
          <p>
            <a href="https://github.com/Elephant333/olympian/tree/main" target="_blank" rel="noopener noreferrer" className="text-blue-500 underline">Github Repo</a>
          </p>
        </div>
      </footer>
    </Container>
  );
}

export default App;
