import streamlit as st
import pickle
import os

st.set_page_config(page_title="Parkinson Disease Prediction", layout="wide")

st.title("🧠 Parkinson Disease Prediction Using Machine Learning")

# Load the model
working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(working_dir, "..", "model", "parkinson_model.pkl")
parkinson_model = pickle.load(open(model_path, "rb"))
st.image("https://img1.wsimg.com/isteam/ip/2d223910-d5a2-4589-92ce-4c337e4cdfd9/How%20to%20use%20Chatgpt%20(26).jpg",use_container_width=True)

with st.container():
    st.markdown("#### Enter the following medical attributes")
    columns = st.columns(3)
    fields = [
        "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)",
        "MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)",
        "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR",
        "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"
    ]
    inputs = []
    for i, field in enumerate(fields):
        with columns[i % 3]:
            inputs.append(st.text_input(field))

# Prediction
parkinson_result = ""
if st.button("Predict Parkinson Disease"):
    try:
        user_input = [float(x) for x in inputs]
        prediction = parkinson_model.predict([user_input])
        parkinson_result = "🧠 The person has Parkinson's disease" if prediction[0] == 1 else "✅ The person does not have Parkinson's disease"
    except ValueError:
        parkinson_result = "⚠️ Please enter valid numerical values."

st.success(parkinson_result)
