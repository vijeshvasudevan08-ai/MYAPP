import streamlit as st
import pickle
import numpy as np
model = pickle.load(open("house_model.pkl", "rb"))
st.title("House Price Prediction")
size = st.number_input("Enter house size (sq ft):", min_value=500, max_value=5000)
bedrooms = st.slider("Number of bedrooms:", 1, 6)
if st.button("Predict"):
    features = np.array([[size, bedrooms]])
    prediction = model.predict(features)[0]
    st.success(f"Predicted Price: ${prediction:,.2f}")