import streamlit as st
from services.predictor import prepare_input_data, display_prediction
from services.api import predict_premium

st.title("Insurance Premium Category Predictor")
st.markdown("Enter your details below:")

age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
)

if st.button("Predict Premium Category"):
    input_data = prepare_input_data(age, weight, height, income_lpa, smoker, city, occupation)
    response = predict_premium(input_data)

    if response["success"]:
        display_prediction(response["data"])
    else:
        st.error(response["error"])
        if "details" in response:
            st.write(response["details"])
