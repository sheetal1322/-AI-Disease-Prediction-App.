# AI Disease Prediction App

A machine learning web app that predicts diseases based on symptoms selected by the user.

## Features
- Predicts top possible diseases from multiple symptoms using a Random Forest model.
- Interactive UI built with Streamlit for easy symptom selection.
- Displays disease prediction probabilities with progress bars.
- Provides a disclaimer to consult a doctor for accurate diagnosis.

## How to Run

1. Clone or download this repository.  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
3. Run the app
   streamlit run app.py
4. Requirements
The app requires these Python packages:
pandas==2.2.3
numpy==2.2.5
scikit-learn
joblib
streamlit==1.45.0
Files in the Repository
app.py — Streamlit application code

disease_model.pkl — Trained Random Forest model

label_encoder.pkl — Label encoder for disease names

requirements.txt — Python dependencies

Notes
This app provides AI-based predictions only. It does NOT replace professional medical advice.

For any health concerns, please consult a healthcare professional.




