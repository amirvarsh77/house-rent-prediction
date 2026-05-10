import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("house_rent_model.pkl", "rb"))

st.title("🏠 House Rent Prediction")

st.write("Enter house details below:")

# User inputs
bhk = st.number_input("BHK", min_value=1, step=1)
size = st.number_input("Size (Square Feet)", min_value=100)
bathroom = st.number_input("Bathrooms", min_value=1, step=1)

# Predict button
if st.button("Predict Rent"):

    # Example input array
    features = np.array([[bhk, size, bathroom]])

    prediction = model.predict(features)

    st.success(f"Predicted Rent: ₹ {prediction[0]:,.2f}")