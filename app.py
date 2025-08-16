import streamlit as st
import pickle
import numpy as np

# File paths
MODEL_PATH = "weather_model.pkl"
ENC_PATH = "label_encoder.pkl"
SCALER_PATH = "scaler.pkl"

# Load model, encoder, scaler
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)
with open(ENC_PATH, "rb") as f:
    label_encoder = pickle.load(f)
with open(SCALER_PATH, "rb") as f:
    scaler = pickle.load(f)

# Streamlit UI
st.set_page_config(page_title="Weather Prediction", layout="centered")
st.title("🌤️ Simple Weather Prediction App")
st.write("Enter values below to predict the weather (sun, rain, drizzle, snow).")

# Inputs
precipitation = st.number_input("Precipitation (mm)", min_value=0.0, value=0.0, step=0.1)
temp_max = st.number_input("Max Temperature (°C)", value=15.0, step=0.1)
temp_min = st.number_input("Min Temperature (°C)", value=5.0, step=0.1)
wind = st.number_input("Wind Speed (km/h)", value=3.0, step=0.1)

# Prediction button
if st.button("Predict Weather"):
    # Prepare input
    X = np.array([[precipitation, temp_max, temp_min, wind]])
    X_scaled = scaler.transform(X)
    
    # Predict
    pred = model.predict(X_scaled)
    pred_label = label_encoder.inverse_transform(pred)[0]
    
    st.success(f"Predicted Weather: {pred_label}")

# Footer / Credit
st.markdown("---")
st.markdown("<h6 style='text-align: center;'>Developed by Bushra</h6>", unsafe_allow_html=True)