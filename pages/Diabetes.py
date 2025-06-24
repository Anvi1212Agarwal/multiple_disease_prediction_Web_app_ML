import streamlit as st
import pickle
import os

st.set_page_config(page_title="Diabetes Prediction", layout="wide")

# Load model
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(os.path.join(working_dir, "..", "model", "diabetes_model.pkl"), "rb"))

st.title("🩺 Diabetes Prediction Using Machine Learning")
st.image("https://www.aimsindia.com/wp-content/uploads/2024/11/26765173_2110.q710.001.P.m005.c20.diabetes-set-scaled.jpg", use_container_width=True)

with st.expander("Enter Patient Details"):
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure")
    with col1:
        SkinThickness = st.text_input("Skin Thickness")
    with col2:
        Insulin = st.text_input("Insulin")
    with col3:
        BMI = st.text_input("BMI")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")
    with col2:
        Age = st.text_input("Age")

diabetes_result = ""
if st.button("Predict Diabetes"):
    try:
        NewBMI_Underweight = NewBMI_Overweight = NewBMI_Obesity_1 = NewBMI_Obesity_2 = NewBMI_Obesity_3 = 0
        NewInsulinScore_Normal = 0
        NewGlucose_Low = NewGlucose_Normal = NewGlucose_Overweight = NewGlucose_Secret = 0

        bmi_val = float(BMI)
        if bmi_val <= 18.5:
            NewBMI_Underweight = 1
        elif 24.9 < bmi_val <= 29.9:
            NewBMI_Overweight = 1
        elif 29.9 < bmi_val <= 34.9:
            NewBMI_Obesity_1 = 1
        elif 34.9 < bmi_val <= 39.9:
            NewBMI_Obesity_2 = 1
        elif bmi_val > 39.9:
            NewBMI_Obesity_3 = 1

        if 16 <= float(Insulin) <= 166:
            NewInsulinScore_Normal = 1

        glucose_val = float(Glucose)
        if glucose_val <= 70:
            NewGlucose_Low = 1
        elif 70 < glucose_val <= 99:
            NewGlucose_Normal = 1
        elif 99 < glucose_val <= 126:
            NewGlucose_Overweight = 1
        elif glucose_val > 126:
            NewGlucose_Secret = 1

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age, NewBMI_Underweight,
                      NewBMI_Overweight, NewBMI_Obesity_1,
                      NewBMI_Obesity_2, NewBMI_Obesity_3, NewInsulinScore_Normal,
                      NewGlucose_Low, NewGlucose_Normal, NewGlucose_Overweight,
                      NewGlucose_Secret]

        user_input = [float(x) for x in user_input]
        prediction = diabetes_model.predict([user_input])
        diabetes_result = "✅ The person has diabetes" if prediction[0] == 1 else "❌ The person has no diabetes"
    except:
        diabetes_result = "⚠️ Please fill all values correctly."

st.success(diabetes_result)
