import streamlit as st
import pickle
import os

st.set_page_config(page_title="Heart Disease Prediction", layout="wide")

working_dir = os.path.dirname(os.path.abspath(__file__))
heart_disease_model = pickle.load(open(os.path.join(working_dir, '../model/heart_model.pkl'), 'rb'))

st.markdown("""
<style>
    .heart-img {
        width: 80%;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    .heart-header {
        color: #FF4B4B;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="heart-header">Heart Disease Prediction Using Machine Learning</div>', unsafe_allow_html=True)
st.image("https://plus.unsplash.com/premium_photo-1717595012923-141a13be88f4?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8aGVhcnQlMjBhbmF0b215JTIwd2l0aCUyMG1hcmtpbmd8ZW58MHx8MHx8fDA%3D", use_container_width=True, caption="Heart Disease Awareness")

with st.expander("Enter Patient Details"):
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex (1 = Male, 0 = Female)")
    with col3:
        cp = st.text_input("Chest Pain Types")

    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Serum Cholestoral in mg/dl")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl (1 = True; 0 = False)")

    with col1:
        restecg = st.text_input("Resting Electrocardiographic results")
    with col2:
        thalach = st.text_input("Maximum Heart Rate achieved")
    with col3:
        exang = st.text_input("Exercise Induced Angina")

    with col1:
        oldpeak = st.text_input("ST depression induced by exercise")
    with col2:
        slope = st.text_input("Slope of the peak exercise ST segment")
    with col3:
        ca = st.text_input("Major vessels colored by flourosopy")

    with col1:
        thal = st.text_input("Thalassemia (1 = Normal; 2 = Fixed defect; 3 = Reversible defect)")

heart_disease_result = ""
if st.button("Predict Heart Disease"):
    try:
        user_input = [
            float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs),
            float(restecg), float(thalach), float(exang), float(oldpeak), float(slope),
            float(ca), float(thal)
        ]
        prediction = heart_disease_model.predict([user_input])
        heart_disease_result = "❤️ The person has heart disease" if prediction[0] == 1 else "💓 The person does not have heart disease"
    except Exception as e:
        heart_disease_result = f"⚠️ Error in prediction: {e}"

st.success(heart_disease_result)
