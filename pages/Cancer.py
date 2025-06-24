import streamlit as st
import pickle
import os

st.set_page_config(page_title="Breast Cancer Prediction", layout="wide")
st.title("🎗️ Breast Cancer Prediction Using Machine Learning")
st.image("https://images.unsplash.com/photo-1579154341098-e4e158cc7f55?q=80&w=1025&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",use_container_width=True)

# Load the model
working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(working_dir, "..", "model", "Breast_model.pkl")
breast_cancer_model = pickle.load(open(model_path, "rb"))

with st.container():
    st.markdown("#### Enter the following medical features")
    columns = st.columns(3)
    fields = [
        "mean radius", "mean texture", "mean perimeter", "mean area", "mean smoothness",
        "mean compactness", "mean concavity", "mean concave points", "mean symmetry",
        "mean fractal dimension", "radius error", "texture error", "perimeter error", "area error",
        "smoothness error", "compactness error", "concavity error", "concave points error", "symmetry error",
        "fractal dimension error", "worst radius", "worst texture", "worst perimeter", "worst area",
        "worst smoothness", "worst compactness", "worst concavity", "worst concave points",
        "worst symmetry", "worst fractal dimension"
    ]
    inputs = []
    for i, field in enumerate(fields):
        with columns[i % 3]:
            inputs.append(st.text_input(field))

# Prediction
cancer_result = ""
if st.button("Predict Breast Cancer"):
    try:
        user_input = [float(x) for x in inputs]
        prediction = breast_cancer_model.predict([user_input])
        cancer_result = "🎗️ The person has Breast Cancer" if prediction[0] == 1 else "✅ The person does not have Breast Cancer"
    except ValueError:
        cancer_result = "⚠️ Please enter valid numerical values."

st.success(cancer_result)
