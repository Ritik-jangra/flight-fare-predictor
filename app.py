import streamlit as st
import pandas as pd
import numpy as np
import joblib
import datetime

# Load model and features
model = joblib.load("random_forest_model.pkl")
model_features = joblib.load("model_features.pkl")

# Set page config
st.set_page_config(page_title="Flight Fare Predictor", layout="centered", page_icon="✈️")

# Custom dark theme styling
st.markdown("""
    <style>
    .main {
        background-color: #0d1117;
        color: white;
    }
    .stApp {
        background-color: #0d1117;
    }
    .stButton button {
        background-color: #5ea6ff;
        color: white;
        border-radius: 10px;
        padding: 0.5em 1em;
        transition: all 0.3s ease;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #2b7efc;
        transform: scale(1.05);
    }
    .stTextInput>div>div>input,
    .stSelectbox>div>div>div {
        background-color: #161b22;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("✈️ Flight Fare Predictor")
st.markdown("Estimate flight fares based on route, airline, stops and schedule.")

# Dropdown options
airlines = ['Air Asia', 'Air India', 'GoAir', 'IndiGo', 'Jet Airways', 
            'Multiple carriers', 'SpiceJet', 'Vistara']
sources = ['Chennai', 'Delhi', 'Kolkata', 'Mumbai', 'Bangalore']
destinations = ['Cochin', 'Delhi', 'Hyderabad', 'Kolkata', 'New Delhi']

# Create a session state variable to control message display
if 'message' not in st.session_state:
    st.session_state.message = ""

if 'last_inputs' not in st.session_state:
    st.session_state.last_inputs = {}

# Form
today = datetime.date.today()
with st.form("input_form"):
    st.markdown("### 📋 Enter Flight Details")

    col1, col2 = st.columns(2)
    with col1:
        airline = st.selectbox("Airline", airlines)
        source = st.selectbox("Source City", sources)
        travel_class = st.selectbox("Class", ["Economy", "Business"])
    with col2:
        destination = st.selectbox("Destination City", destinations)
        total_stops = st.selectbox("Total Stops", ['zero', 'one', 'two_or_more'])

    col3, col4 = st.columns(2)
    with col3:
        dep_date = st.date_input("Departure Date", today, min_value=today)
        dep_time = st.time_input("Departure Time", datetime.time(10, 0))
    with col4:
        arr_date = st.date_input("Arrival Date", today, min_value=today)
        arr_time = st.time_input("Arrival Time", datetime.time(12, 0))

    submitted = st.form_submit_button("Predict Fare")

# Combine current inputs
current_inputs = {
    "airline": airline,
    "source": source,
    "destination": destination,
    "travel_class": travel_class,
    "total_stops": total_stops,
    "dep_date": dep_date,
    "dep_time": dep_time,
    "arr_date": arr_date,
    "arr_time": arr_time,
}

# Clear previous message if input has changed
if current_inputs != st.session_state.last_inputs:
    st.session_state.message = ""

# On submit
if submitted:
    st.session_state.last_inputs = current_inputs.copy()
    dep_datetime = datetime.datetime.combine(dep_date, dep_time)
    arr_datetime = datetime.datetime.combine(arr_date, arr_time)

    if arr_datetime <= dep_datetime:
        st.session_state.message = {
            "type": "error",
            "text": "❌ Arrival must be after departure. Please correct the date/time."
        }
    else:
        # Extract features
        data = {
            "stops": {"zero": 0, "one": 1, "two_or_more": 2}[total_stops],
            "class": {"Economy": 0, "Business": 1}[travel_class],
            "Journey_day": dep_date.day,
            "Journey_month": dep_date.month,
            "Dep_hour": dep_time.hour,
            "Dep_min": dep_time.minute,
            "Arrival_hour": arr_time.hour,
            "Arrival_min": arr_time.minute,
            "Duration_hour": abs(arr_time.hour - dep_time.hour),
            "Duration_min": abs(arr_time.minute - dep_time.minute),
        }

        input_df = pd.DataFrame([data])
        input_df["airline"] = airline
        input_df["source_city"] = source
        input_df["destination_city"] = destination
        input_df["departure_time"] = "Unknown"
        input_df["arrival_time"] = "Unknown"

        input_df = pd.get_dummies(input_df)
        input_df = input_df.reindex(columns=model_features, fill_value=0)

        prediction = model.predict(input_df)[0]
        st.session_state.message = {
            "type": "success",
            "text": f"✅ Estimated Flight Fare: ₹ {round(prediction, 2)}"
        }

# Display message if present
if st.session_state.message:
    if st.session_state.message["type"] == "success":
        st.success(st.session_state.message["text"])
    elif st.session_state.message["type"] == "error":
        st.error(st.session_state.message["text"])
