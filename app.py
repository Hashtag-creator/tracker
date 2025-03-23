import streamlit as st
import requests

st.title("AI-Powered Health Tracker")

st.header("Fitness Tracking")
steps = st.number_input("Enter Steps Walked", min_value=0)
if st.button("Predict Calories Burned"):
    try:
        response = requests.post("http://127.0.0.1:5000/predict_calories", json={"steps": steps})
        response.raise_for_status()
        st.write("Calories Burned:", response.json().get('calories_burned', 'Error in response'))
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")

st.header("Diet Recommendation")
goal = st.selectbox("Choose Goal", ["weight_loss", "muscle_gain", "balanced"])
if st.button("Get Diet Plan"):
    try:
        response = requests.get(f"http://127.0.0.1:5000/diet?goal={goal}")
        response.raise_for_status()
        st.write("Diet Plan:", response.json().get('diet_plan', 'Error in response'))
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")

st.header("Sleep Analysis")
hours = st.number_input("Enter Sleep Hours", min_value=0)
if st.button("Check Sleep Quality"):
    try:
        response = requests.post("http://127.0.0.1:5000/sleep", json={"hours": hours})
        response.raise_for_status()
        st.write("Sleep Quality:", response.json().get('sleep_quality', 'Error in response'))
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")

st.header("Disease Risk Prediction")
age = st.number_input("Enter Age", min_value=0)
bmi = st.number_input("Enter BMI", min_value=0.0)
if st.button("Check Disease Risk"):
    try:
        response = requests.post("http://127.0.0.1:5000/disease", json={"age": age, "bmi": bmi})
        response.raise_for_status()
        st.write("Risk Level:", response.json().get('disease_risk', 'Error in response'))
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
