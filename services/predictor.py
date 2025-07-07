import streamlit as st

def prepare_input_data(age, weight, height, income_lpa, smoker, city, occupation) -> dict:
    return {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

def display_prediction(result: dict):
    category = result.get("predicted_category", "N/A")
    confidence = result.get("confidence", "N/A")
    probabilities = result.get("class_probabilities", {})

    st.success(f"Predicted Insurance Premium Category: **{category}**")
    st.write(f"Confidence Score: **{confidence}**")
    st.write("Class Probabilities:")
    for label, prob in probabilities.items():
        st.write(f"- {label}: {prob}")