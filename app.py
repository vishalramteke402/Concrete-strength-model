import streamlit as st
import numpy as np
import pickle

# Load model
with open("concrete_strength.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🧱 Concrete Compressive Strength Predictor (MPa)")
st.write("Enter the concrete mix proportions to predict compressive strength.")

# Input fields
cement = st.number_input("Cement (kg/m³)", min_value=0.0, step=1.0)
slag = st.number_input("Slag (kg/m³)", min_value=0.0, step=1.0)
flyash = st.number_input("Fly Ash (kg/m³)", min_value=0.0, step=1.0)
water = st.number_input("Water (kg/m³)", min_value=0.0, step=1.0)
superplasticizer = st.number_input("Superplasticizer (kg/m³)", min_value=0.0, step=1.0)
coarseaggregate = st.number_input("Coarse Aggregate (kg/m³)", min_value=0.0, step=1.0)
fineaggregate = st.number_input("Fine Aggregate (kg/m³)", min_value=0.0, step=1.0)
age = st.number_input("Age (days)", min_value=1, step=1)

# Prediction
if st.button("Predict Strength"):
    features = np.array([[cement, slag, flyash, water, superplasticizer,
                          coarseaggregate, fineaggregate, age]])

    prediction = model.predict(features)[0]

    st.success(f"Predicted Concrete Strength: **{prediction:.2f} MPa**")
