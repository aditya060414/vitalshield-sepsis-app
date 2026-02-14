VitalShield: AI-Powered Sepsis Prediction
🚀 Live Demo
Access the live, deployed prototype here:


➡️ https://vitalshield-sepsis-app-faettuz7bbwkwtskxv8siy.streamlit.app/

📖 About The Project
VitalShield is a machine learning-powered web application designed to predict the risk of sepsis in ICU patients. It provides a simple, high-fidelity prototype interface for clinicians to input a patient's latest vital signs and lab results, receiving an immediate, actionable risk score (e.g., "HIGH RISK" or "LOW RISK").

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
