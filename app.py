import pickle
from nbformat import write
import streamlit as st
from streamlit_lottie import st_lottie
import requests


st.set_page_config(page_title='Fraud-Detection', page_icon=':computer:', layout="wide")



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl('https://assets7.lottiefiles.com/packages/lf20_5tl1xxnz.json')

pickle_in = open("rf_model.pkl", "rb")
model = pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_insurance_fraud(Area_Service, Age, Gender, Cultural_group, ethnicity, Admission_type, Home_or_Selfcare,
                            ccs_procedure_code, Code_illness, Mortality_risk, Surg_Description, Weight_baby,
                            Emergency_dept_yes_No,Tot_charg,ratio_of_total_costs_to_total_charges, Payment_Typology):
    prediction = model.predict([[Area_Service, Age, Gender, Cultural_group, ethnicity, Admission_type, Home_or_Selfcare,
                                 ccs_procedure_code, Code_illness, Mortality_risk, Surg_Description, Weight_baby,
                                 Emergency_dept_yes_No,Tot_charg, ratio_of_total_costs_to_total_charges,Payment_Typology]])
    print(prediction)
    if prediction == 0:
        return "The claim is FRAUD."
    else:
        return 'The claim is GENUINE.'


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Fraud Detection App")
        html_temp = """
        <div style="background-color:#03286b;padding:10px">
        <h2 style="color:white;text-align:center;">Insurance Fraud Detection</h2>
        </div>
        """
        st.subheader(" Hi! :wave: Welcome to the Fraud Detection App :page_with_curl:")
        st.write("- Health insurance in India is a growing segment of India's economy.")
        st.write("- The life insurance industry is expected to increase at a CAGR of 5.3% between 2019 and 2023. India’s insurance penetration was pegged at 4.2% in FY21, with life insurance penetration at 3.2% and non-life insurance penetration at 1.0%. In terms of insurance density, India’s overall density stood at US$ 78 in FY21.")
        st.write("- Premiums from India’s life insurance industry is expected to reach Rs. 24 lakh crore (US$ 317.98 billion) by FY31.")
        st.write("- The Indian healthcare system is one of the largest in the world, with the number of people it concerns : nearly 1.3 billion potential beneficiaries.")
        st.write("- As the number of claims in India is increasing, the need for a robust and accurate fraud detection system is growing.")
        st.write("- This app is a simple fraud detection system for Indian insurance claims which will tell you whether the claim is genuine or fraud.")
    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")

    st.markdown(html_temp, unsafe_allow_html=True)

with st.form(key='my_form'):
    Area_Service = st.selectbox("Area Service", (
        'Western NY', 'Finger Lakes', 'Southern Tier', 'Central NY', 'Capital/Adirond', 'Hudson Valley',
        'New York City'))
    Age = st.selectbox("Age of person", ('0 to 17', '18 to 29', '30 to 49', '50 to 69', '70 or Older'))
    Gender = st.selectbox("Gender",('Female', 'Male'))
    Cultural_group = st.selectbox("Cultural Group", ('White', 'Black/African American', 'Other Race'))
    ethnicity = st.selectbox("Ethnicity", ('Not Span/Hispanic', 'Spanish/Hispanic'))
    Admission_type = st.selectbox("Admission Type", ('Elective', 'Urgent', 'Emergency', 'Newborn', 'Trauma'))
    Home_or_Selfcare = st.selectbox("Home or Selfcare", (
        'Home or Self Care', 'Short-term Hospital', 'Hosp Basd Medicare Approved Swing Bed',
        'Facility w/ Custodial/Supportive Care', 'Skilled Nursing Home', 'Expired', 'Left Against Medical Advice',
        'Home w/ Home Health Services', 'Psychiatric Hospital or Unit of Hosp', 'Hospice - Home',
        'Hospice - Medical Facility', 'Federal Health Care Facility', 'Inpatient Rehabilitation Facility',
        "Cancer Center or Children's Hospital", 'Court/Law Enforcement',
        'Medicare Cert Long Term Care Hospital', 'Another Type Not Listed', 'Critical Access Hospital',
        'Medicaid Cert Nursing Facility'))
    ccs_procedure_code = st.number_input("CCS Procedure Code", min_value=0, max_value=250)
    Code_illness = st.selectbox("Code Illness", ('1', '2', '3', '4'))
    Mortality_risk = st.selectbox("Mortality Risk", ('1.0', '2.0', '3.0', '4.0'))
    Surg_Description = st.selectbox("Surgical Description", ('Medical', 'Surgical'))
    Weight_baby = st.number_input("Weight of the Baby", min_value=0, max_value=9000)
    Emergency_dept_yes_No = st.selectbox("Emergency Department (Yes or No)", ('Y', 'N'))
    Tot_charg = st.number_input("Total charge",min_value=0,max_value=6600000)
    ratio_of_total_costs_to_total_charges = st.number_input('Ratio of total cost and total charge',min_value=0.0,max_value=200.0)

    Payment_Typology = st.selectbox("Payment Typology", ('1', '2', '3', '4', '5'))
    #submit_button = st.form_submit_button(label='Submit')

    result = ""

    if st.form_submit_button('Predict'):
        result = predict_insurance_fraud(Area_Service, Age, Gender, Cultural_group, ethnicity, Admission_type,
                                         Home_or_Selfcare, ccs_procedure_code, Code_illness, Mortality_risk,
                                         Surg_Description, Weight_baby, Emergency_dept_yes_No,Tot_charg,
                                         ratio_of_total_costs_to_total_charges,Payment_Typology)

    st.success(result)
    if st.form_submit_button("About"):
        st.text("Built by Aishwarya Mate")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    print('Predicted')
