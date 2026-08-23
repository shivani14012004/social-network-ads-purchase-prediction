import streamlit as st
import pickle
import pandas as pd

# --------------------------------
# Page Title
# --------------------------------
st.title("🛍️ Social Network Ads - KNN")

st.write("Predict whether a customer will purchase a product or not.")


# --------------------------------
# Load KNN With Scaling Model
# --------------------------------
with open("knn_with_scaling.pkl", "rb") as file:
    knn_model = pickle.load(file)


# --------------------------------
# Load Scaler
# --------------------------------
with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)


# --------------------------------
# User Input
# --------------------------------

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

salary = st.number_input(
    "Estimated Salary",
    min_value=0,
    max_value=500000,
    value=50000
)


# --------------------------------
# Convert Gender into Number
# --------------------------------

if gender == "Male":
    gender_encoded = 1
else:
    gender_encoded = 0


# --------------------------------
# Prediction Button
# --------------------------------

if st.button("Predict"):

    # Create input DataFrame
    input_data = pd.DataFrame(
        [[gender_encoded, age, salary]],
        columns=["Gender", "Age", "EstimatedSalary"]
    )

    # Apply Feature Scaling
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = knn_model.predict(input_scaled)

    # Probability
    probability = knn_model.predict_proba(input_scaled)


    # --------------------------------
    # Display Accuracy
    # --------------------------------

    st.write("### Model Information")
    st.write("Algorithm: **KNN with Feature Scaling**")
    st.write("K Value: **5**")
    st.write("Accuracy: **92.5%**")


    # --------------------------------
    # Display Result
    # --------------------------------

    if prediction[0] == 1:

        st.success("✅ Customer will Purchase!")

        st.write(
            "Purchase Probability:",
            round(probability[0][1] * 100, 2),
            "%"
        )

        st.write(
            "Not Purchase Probability:",
            round(probability[0][0] * 100, 2),
            "%"
        )

    else:

        st.error("❌ Customer will Not Purchase!")

        st.write(
            "Not Purchase Probability:",
            round(probability[0][0] * 100, 2),
            "%"
        )

        st.write(
            "Purchase Probability:",
            round(probability[0][1] * 100, 2),
            "%"
        )