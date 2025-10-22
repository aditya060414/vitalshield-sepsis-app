import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- This is the "Bolts" part ---
# This is our web app front-end

# 1. Load the saved model and columns
try:
    model = joblib.load('sepsis_model.pkl')
    model_columns = joblib.load('model_columns.pkl')
    print("Model and columns loaded successfully.")
except FileNotFoundError:
    st.error("Error: Model files (sepsis_model.pkl or model_columns.pkl) not found.")
    st.stop() # Stop the app if we can't load the model

# 2. Create the User Interface (UI)
st.title('VitalShield Sepsis Prediction 🩺')
st.markdown("Enter the patient's latest vital signs and lab results to predict sepsis risk.")

# Create input fields in the sidebar
st.sidebar.header('Patient Input Features')

# Define input fields with realistic min/max/default values
age = st.sidebar.number_input('Age', min_value=18, max_value=120, value=65)
gender = st.sidebar.selectbox('Gender', ('Male', 'Female'))

# Vitals
heart_rate = st.sidebar.number_input('Heart Rate (bpm)', min_value=30, max_value=250, value=80)
bp_systolic = st.sidebar.number_input('Systolic BP (mmHg)', min_value=50, max_value=250, value=120)
bp_diastolic = st.sidebar.number_input('Diastolic BP (mmHg)', min_value=30, max_value=150, value=80)
resp_rate = st.sidebar.number_input('Respiratory Rate (insp/min)', min_value=5, max_value=60, value=18)
temp_f = st.sidebar.number_input('Temperature (°F)', min_value=90.0, max_value=108.0, value=98.6, format="%.1f")

# Labs
lactate = st.sidebar.number_input('Lactate (mmol/L)', min_value=0.1, max_value=30.0, value=2.3, format="%.1f")
wbc = st.sidebar.number_input('WBC Count (K/uL)', min_value=0.1, max_value=100.0, value=9.5, format="%.1f")


# 3. Create the "Predict" Button
if st.button('Predict Sepsis Risk'):
    
    # 4. Prepare the input data for the model
    
    # Create a dictionary of all the features
    # This MUST match the columns from Step 14
    input_data = {
        'anchor_age': age,
        'BP_DIASTOLIC_max': bp_diastolic,
        'BP_SYSTOLIC_max': bp_systolic,
        'HEART_RATE_max': heart_rate,
        'RESP_RATE_max': resp_rate,
        'TEMP_F_max': temp_f,
        'LACTATE_max': lactate,
        'WBC_max': wbc,
        'gender_M': 1 if gender == 'Male' else 0
    }
    
    # Convert to a pandas DataFrame
    # We use model_columns to make 100% sure the order is correct
    input_df = pd.DataFrame([input_data])
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    # 5. Make the prediction
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df) # Get probabilities

    # 6. Display the result
    sepsis_probability = prediction_proba[0][1] # Probability of '1' (Sepsis)

    if prediction[0] == 1:
        st.error(f'**HIGH RISK: Sepsis Predicted** (Risk Score: {sepsis_probability*100:.0f}%)')
        st.markdown("Recommend immediate clinical review and sepsis protocol.")
        
    else:
        st.success(f'**LOW RISK: Sepsis Not Predicted** (Risk Score: {sepsis_probability*100:.0f}%)')
        st.markdown("Continue standard monitoring.")