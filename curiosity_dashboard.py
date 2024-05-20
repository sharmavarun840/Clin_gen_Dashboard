import streamlit as st
import pandas as pd
import plotly.express as px
import graphviz as gv

# Sample patient data
patient_info = {
    "Name": "John Doe",
    "Age": 45,
    "Clinical Classification": "Hypertension"
}

biochemical_parameters = {
    "Parameter": ["Cholesterol", "HDL", "LDL", "Triglycerides", "Blood Glucose", "Blood Pressure"],
    "Value": [250, 35, 160, 180, 110, 140],
    "Reference Range": ["< 200 mg/dL", "> 40 mg/dL", "< 100 mg/dL", "< 150 mg/dL", "< 100 mg/dL", "120/80 mmHg"]
}

pharmacogenomics = {
    "Gene": ["CYP2C19"],
    "Genotype": ["Poor Metaboliser"]
}

polygenic_risk_score = {
    "Trait": ["Cardiovascular Disease"],
    "Risk Score": ["High"]
}

family_history = {
    "Relative": ["Father", "Mother", "Brother", "Sister"],
    "Condition": ["Hypertension", "Diabetes", "Hypertension", "None"]
}

echo_findings = {
    "Finding": ["Left Ventricular Hypertrophy", "Ejection Fraction", "Aortic Stenosis"],
    "Result": ["Present", "55%", "None"]
}

mri_findings = {
    "Finding": ["Brain Lesions", "Spinal Cord Lesions"],
    "Result": ["None", "None"]
}

# Convert dictionaries to DataFrames
biochemical_df = pd.DataFrame(biochemical_parameters)
pharmacogenomics_df = pd.DataFrame(pharmacogenomics)
polygenic_risk_score_df = pd.DataFrame(polygenic_risk_score)
family_history_df = pd.DataFrame(family_history)
echo_findings_df = pd.DataFrame(echo_findings)
mri_findings_df = pd.DataFrame(mri_findings)

# Set up the Streamlit app
st.set_page_config(page_title="Curiosity Dashboard", layout="wide")
st.image("https://via.placeholder.com/150x50", caption="Curiosity - Powered by NMC Genetics", use_column_width=True)
st.title("Patient Biochemical Parameters Dashboard")

# Display patient information
st.header("Patient Information")
st.image("https://via.placeholder.com/150", caption="Patient Photo", width=150)
st.write(f"**Name:** {patient_info['Name']}")
st.write(f"**Age:** {patient_info['Age']}")
st.write(f"**Clinical Classification:** {patient_info['Clinical Classification']}")

# Function to highlight high values
def highlight_high_values(row):
    conditions = [
        (row['Parameter'] == "Cholesterol" and row['Value'] >= 200),
        (row['Parameter'] == "HDL" and row['Value'] <= 40),
        (row['Parameter'] == "LDL" and row['Value'] >= 100),
        (row['Parameter'] == "Triglycerides" and row['Value'] >= 150),
        (row['Parameter'] == "Blood Glucose" and row['Value'] >= 100),
        (row['Parameter'] == "Blood Pressure" and row['Value'] >= 120)
    ]
    return ['background-color: red' if any(conditions) else '' for _ in row]

# Display biochemical parameters
st.header("Biochemical Parameters")
st.dataframe(biochemical_df.style.apply(highlight_high_values, axis=1))

# Display pharmacogenomics data
st.header("Pharmacogenomics")
st.dataframe(pharmacogenomics_df.style.applymap(lambda x: 'background-color: lightblue'))

# Display polygenic risk score
st.header("Polygenic Risk Score")
st.dataframe(polygenic_risk_score_df.style.applymap(lambda x: 'background-color: lightyellow'))

# Display family history
st.header("Family History")
st.dataframe(family_history_df.style.applymap(lambda x: 'background-color: lightgreen'))

# Display echo findings
st.header("Echo Findings")
st.dataframe(echo_findings_df.style.applymap(lambda x: 'background-color: lightcoral'))

# Display MRI findings
st.header("MRI Findings")
st.dataframe(mri_findings_df.style.applymap(lambda x: 'background-color: lightcyan'))

# Pedigree chart using Graphviz
st.header("Pedigree Chart")
pedigree = gv.Digraph()
pedigree.node('Patient', 'John Doe')
pedigree.node('Father', 'Father')
pedigree.node('Mother', 'Mother')
pedigree.node('Brother', 'Brother')
pedigree.node('Sister', 'Sister')
pedigree.edge('Father', 'Patient')
pedigree.edge('Mother', 'Patient')
pedigree.edge('Father', 'Brother')
pedigree.edge('Mother', 'Brother')
pedigree.edge('Father', 'Sister')
pedigree.edge('Mother', 'Sister')
st.graphviz_chart(pedigree)

# Interactive elements
if st.checkbox('Show Reference Ranges'):
    st.write("""
    **Reference Ranges:**
    - Cholesterol: < 200 mg/dL
    - HDL: > 40 mg/dL
    - LDL: < 100 mg/dL
    - Triglycerides: < 150 mg/dL
    - Blood Glucose: < 100 mg/dL
    - Blood Pressure: 120/80 mmHg
    """)

# Instructions to run the Streamlit app
st.sidebar.title("Instructions")
st.sidebar.write("""
1. Ensure you have Streamlit installed: `pip install streamlit`
2. Save this script as `curiosity_dashboard.py`
3. Run the script using: `streamlit run curiosity_dashboard.py`
""")

# Additional customization
st.sidebar.title("Settings")
theme = st.sidebar.radio("Choose Theme", ["Default", "Dark", "Light"])
if theme == "Dark":
    st.write('<style>body {background-color: #111; color: white;}</style>', unsafe_allow_html=True)
elif theme == "Light":
    st.write('<style>body {background-color: #fff; color: black;}</style>', unsafe_allow_html=True)
else:
    st.write('<style>body {background-color: #f0f2f6; color: black;}</style>', unsafe_allow_html=True)
