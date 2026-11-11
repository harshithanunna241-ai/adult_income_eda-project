import streamlit as st
import joblib

# Page configuration
st.set_page_config(
    page_title="Adult Income Prediction",
    page_icon="💰"
)

# Title
st.title("💰 Adult Income Prediction")

st.write(
    "Enter the person's details to predict whether "
    "the annual income is <=50K or >50K."
)


# Load model and scaler
model = joblib.load("models/income_model.pkl")
scaler = joblib.load("models/scaler.pkl")


# -----------------------------
# Input fields
# -----------------------------

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

workclass = st.selectbox(
    "Workclass",
    [
        "Private",
        "Self-emp-not-inc",
        "Self-emp-inc",
        "Federal-gov",
        "Local-gov",
        "State-gov",
        "Without-pay",
        "Never-worked",
        "Unknown"
    ]
)

education = st.selectbox(
    "Education",
    [
        "Bachelors",
        "Some-college",
        "11th",
        "HS-grad",
        "Prof-school",
        "Assoc-acdm",
        "Assoc-voc",
        "9th",
        "7th-8th",
        "12th",
        "Masters",
        "1st-4th",
        "10th",
        "Doctorate",
        "5th-6th",
        "Preschool"
    ]
)

education_num = st.number_input(
    "Education Number",
    min_value=1,
    max_value=16,
    value=10
)

marital_status = st.selectbox(
    "Marital Status",
    [
        "Married-civ-spouse",
        "Divorced",
        "Never-married",
        "Separated",
        "Widowed",
        "Married-spouse-absent",
        "Married-AF-spouse"
    ]
)

occupation = st.selectbox(
    "Occupation",
    [
        "Tech-support",
        "Craft-repair",
        "Other-service",
        "Sales",
        "Exec-managerial",
        "Prof-specialty",
        "Handlers-cleaners",
        "Machine-op-inspct",
        "Adm-clerical",
        "Farming-fishing",
        "Transport-moving",
        "Priv-house-serv",
        "Protective-serv",
        "Armed-Forces",
        "Unknown"
    ]
)

relationship = st.selectbox(
    "Relationship",
    [
        "Wife",
        "Own-child",
        "Husband",
        "Not-in-family",
        "Other-relative",
        "Unmarried"
    ]
)

race = st.selectbox(
    "Race",
    [
        "White",
        "Black",
        "Asian-Pac-Islander",
        "Amer-Indian-Eskimo",
        "Other"
    ]
)

sex = st.selectbox(
    "Sex",
    [
        "Male",
        "Female"
    ]
)

capital_gain = st.number_input(
    "Capital Gain",
    min_value=0,
    value=0
)

capital_loss = st.number_input(
    "Capital Loss",
    min_value=0,
    value=0
)

hours_per_week = st.number_input(
    "Hours per Week",
    min_value=1,
    max_value=100,
    value=40
)

native_country = st.selectbox(
    "Native Country",
    [
        "United-States",
        "Cambodia",
        "England",
        "Puerto-Rico",
        "Canada",
        "Germany",
        "Outlying-US(Guam-USVI-etc)",
        "India",
        "Japan",
        "Greece",
        "South",
        "China",
        "Cuba",
        "Iran",
        "Honduras",
        "Philippines",
        "Italy",
        "Poland",
        "Jamaica",
        "Vietnam",
        "Mexico",
        "Portugal",
        "Ireland",
        "France",
        "Dominican-Republic",
        "Laos",
        "Ecuador",
        "Taiwan",
        "Haiti",
        "Columbia",
        "Hungary",
        "Guatemala",
        "Nicaragua",
        "Scotland",
        "Thailand",
        "Yugoslavia",
        "El-Salvador",
        "Trinadad&Tobago",
        "Peru",
        "Hong",
        "Holand-Netherlands",
        "Unknown"
    ]
)


