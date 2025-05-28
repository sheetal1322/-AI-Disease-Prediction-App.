import streamlit as st
import pandas as pd
import joblib

# Load model and encoder
model = joblib.load("disease_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Get all symptoms used during training
all_symptoms = model.feature_names_in_

# App UI
st.set_page_config(page_title="AI Disease Predictor", layout="centered")
st.title("🧠 AI-Based Disease Prediction App")
st.markdown("### Select your symptoms and get the top possible disease predictions.")

# Symptom multi-select
selected_symptoms = st.multiselect("🩺 Symptoms (select multiple):", sorted(all_symptoms))

if st.button("🔍 Predict Disease"):
    if not selected_symptoms:
        st.warning("⚠️ Please select at least one symptom.")
    else:
        # Convert selected symptoms to binary input vector
        input_vector = [1 if symptom in selected_symptoms else 0 for symptom in all_symptoms]

        # Predict probabilities
        probabilities = model.predict_proba([input_vector])[0]
        top_indices = probabilities.argsort()[-3:][::-1]  # Top 3 predictions

        # Display top predictions
        st.subheader("📊 Top Predicted Diseases:")
        for idx in top_indices:
            disease = label_encoder.inverse_transform([idx])[0]
            prob = probabilities[idx] * 100
            st.markdown(f"**{disease}** - {prob:.2f}% probability")
            st.progress(min(int(prob), 100))  # progress bar

        st.info("💡 These predictions are based on selected symptoms. Consult a doctor for accurate diagnosis.")
