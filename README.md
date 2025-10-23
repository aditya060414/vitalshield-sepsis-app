VitalShield: AI-Powered Sepsis Prediction
🚀 Live Demo
Access the live, deployed prototype here:


➡️ https://vitalshield-sepsis-app-faettuz7bbwkwtskxv8siy.streamlit.app/

📖 About The Project
VitalShield is a machine learning-powered web application designed to predict the risk of sepsis in ICU patients. It provides a simple, high-fidelity prototype interface for clinicians to input a patient's latest vital signs and lab results, receiving an immediate, actionable risk score (e.g., "HIGH RISK" or "LOW RISK").

The core mission of this project is to provide an early warning system, as sepsis mortality is known to increase by up to 8% for every hour that treatment is delayed.

🏆 Hackathon Context
This project is a submission for the innoWAH! 2025-26 innovation competition. The theme is "Engineering solutions with Bytes & Bolts".

VitalShield addresses this theme by combining:

The "Bytes" 🧠: A predictive AI model (Logistic Regression) trained on the public MIMIC-IV dataset. The entire data processing and model training pipeline is documented in the analysis.ipynb notebook, achieving 92.31% accuracy on the unseen test set.

The "Bolts" 🔩: A hands-on, interactive web dashboard (app.py) built with Streamlit. This app serves as the functional "Bolt" interface, loading the trained model and putting its predictive power directly into the hands of a (simulated) end-user.

🛠️ How It Was Built
The project is broken into two main parts:

1. The "Bytes": AI Model Training (analysis.ipynb)
Data Sourcing: The project uses the MIMIC-IV Clinical Database Demo, a set of 128 ICU patients.

Data Labeling: Patients were labeled as "Sepsis" (1) or "Non-Sepsis" (0) by cross-referencing diagnoses_icd.csv with a comprehensive list of known sepsis-related ICD codes.

Feature Engineering: Key vitals (Heart Rate, Blood Pressure, Temp, Resp. Rate) and labs (Lactate, WBC Count) were extracted from chartevents.csv and labevents.csv. The worst (maximum) value for each patient during their stay was used as a feature.

Imputation: Missing lab values (e.g., Lactate) were filled using the median value from the dataset.

Training: A Logistic Regression model was trained on the cleaned, engineered dataset. The final model (sepsis_model.pkl) and its required column order (model_columns.pkl) were saved to disk.

2. The "Bolts": Streamlit Dashboard (app.py)
A simple UI is built with Streamlit, providing sidebar inputs for a patient's key features.

The app loads the saved sepsis_model.pkl and model_columns.pkl files on startup.

When the "Predict" button is clicked, the app:

Collects the 8 user inputs.

Formats them into a single-row pandas DataFrame, ensuring the columns exactly match the order the model was trained on.

Calls model.predict_proba() to get a percentage risk score.

Displays a "HIGH RISK" or "LOW RISK" message with the final probability.

📁 Key Files
├── app.py                   # The Streamlit web app
├── analysis.ipynb           # Jupyter Notebook with all data processing and model training
├── sepsis_model.pkl         # The saved, trained AI model
├── model_columns.pkl        # The saved list of model feature columns
├── requirements.txt         # Required Python libraries for deployment
├── VitalShield.pdf          # The original hackathon pitch deck
└── README.md                # You are here!
⚙️ How to Run Locally
To run this project on your own machine:

Clone the repository:

Bash

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install dependencies:

Bash

pip install -r requirements.txt
Run the app:

Bash

streamlit run app.py
