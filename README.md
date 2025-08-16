# 🌦 Simple Weather Prediction App

This project is a **Machine Learning powered Weather Prediction App** built with **Streamlit**.  
It predicts the type of weather such as **☀️ Sun, 🌧️ Rain, 🌦️ Drizzle, or ❄️ Snow** based on user inputs like precipitation, temperature, and wind speed.  

---

## 📸 Demo Screenshot

![App Screenshot](./screenshot.png)

*(Above: Example interface of the Streamlit app)*

---

## 📌 Features
- User-friendly **Streamlit web interface**  
- Takes input values:
  - Precipitation (mm)  
  - Max Temperature (°C)  
  - Min Temperature (°C)  
  - Wind Speed (km/h)  
- Predicts: **Sun / Rain / Drizzle / Snow**  
- Clean dark-themed UI  
- "Developed by Bushra" branding at the bottom  

---

## 📂 Project Structure
weather-prediction-app/
│
├── data/ # Dataset folder
│ └── weather_data.csv
│
├── notebooks/ # Jupyter notebooks
│ └── weather_prediction.ipynb
│
├── src/ # Source code
│ ├── preprocess.py
│ ├── model.py
│ └── predict.py
│
├── app.py # Streamlit frontend app
├── requirements.txt # Dependencies
├── weather_model.pkl # Trained model (saved)
├── screenshot.png # App screenshot
└── README.md # Project documentation
