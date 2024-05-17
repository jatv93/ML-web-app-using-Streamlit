from pickle import load
import streamlit as st

model = load(open("../models/tree_classifier_crit-entro_maxdepth-5_minleaf-4_minsplit2_42.sav", "rb"))
class_dict = {
    "0": "Negative Possibility",
    "1": "Positive Possibility"
}

st.title("Diabetes - Model prediction")

val1 = st.slider("Pregnancies", min_value = 0.0, max_value = 10.0, step = 0.1)
val2 = st.slider("Glucose", min_value = 0.0, max_value = 200.0, step = 0.1)
val3 = st.slider("Blood Preasure", min_value = 0.0, max_value = 100.0, step = 0.1)
val4 = st.slider("Insulin", min_value = 0.0, max_value = 100.0, step = 0.1)
val5 = st.slider("BMI", min_value = 0.0, max_value = 100.0, step = 0.1)
val6 = st.slider("Diabetes Pedigree Function", min_value = 0.0, max_value = 100.0, step = 0.1)
val7 = st.slider("Age", min_value = 0.0, max_value = 100.0, step = 0.1)


if st.button("Predict"):
    prediction = str(model.predict([[val1, val2, val3, val4, val5, val6, val7]])[0])
    pred_class = class_dict[prediction]
    st.write("Prediction:", pred_class)