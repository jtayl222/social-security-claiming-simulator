import streamlit as st
import requests
import pandas as pd
import uuid  # For generating unique session IDs

st.title("Social Security Claiming Strategies")

st.markdown("""
This application compares two claiming strategies using FastAPI as a backend and 
Streamlit as the frontend.

**How to find your FRA benefit:**  
Log into your Social Security account and review your statement – your 
"Primary Insurance Amount" (PIA) is the benefit you’d receive at Full Retirement Age (FRA).  
Enter that monthly amount below.
""")

# Basic inputs
birthdate = st.text_input(
    "Enter your birthdate (YYYY-MM-DD):", 
    "1960-01-01",
    help="Enter your birthdate in the format YYYY-MM-DD. This is used to calculate your current age."
)
fra_benefit = st.number_input(
    "Your monthly benefit at FRA (from your Social Security statement):", 
    min_value=0.0, 
    value=3000.0,
    help="Enter the monthly benefit amount as stated in your Social Security statement for Full Retirement Age."
)
age_model1 = st.number_input(
    "Claiming Age for Model 1 (≥ 62):", 
    min_value=62, 
    max_value=100, 
    value=65,
    help="Enter the age at which you plan to claim Social Security benefits in Model 1. Must be at least 62."
)
age_model2 = st.number_input(
    "Claiming Age for Model 2 (≥ 62):", 
    min_value=62, 
    max_value=100, 
    value=70,
    help="Enter the age at which you plan to claim Social Security benefits in Model 2. Must be at least 62."
)

st.markdown("## Financial Parameters")
inflation_rate = st.number_input(
    "Inflation Rate (decimal):", 
    value=0.04,
    help="Enter the expected annual inflation rate as a decimal (e.g., 0.04 for 4%)."
)
investment_return = st.number_input(
    "Investment Return (decimal):", 
    value=0.05,
    help="Enter the expected annual return on your investments as a decimal (e.g., 0.05 for 5%)."
)
filing_status = st.selectbox(
    "Filing Status:", 
    options=["Single", "Married Filing Jointly", "Married Filing Separately", "Head of Household"],
    help="Select your tax filing status. This affects tax-related calculations and deductions in the simulation."
)
initial_401k = st.number_input(
    "Initial 401(k) Balance:", 
    value=1000000.0,
    help="Enter the current value of your 401(k) retirement account."
)
other_non_retirement_savings = st.number_input(
    "Other Non-Retirement Savings:", 
    value=500000.0,
    help="Enter the total amount of your savings that are not in retirement accounts."
)
target_income = st.number_input(
    "Target Monthly Income:", 
    value=9000.0,
    help="Enter the monthly income amount you aim to achieve during retirement. Withdrawal calculations are based on this value."
)
non_retirement_gain_percentage = st.number_input(
    "Non-Retirement Gain Percentage (decimal):", 
    value=0.50,
    help="Enter the expected annual gain for your non-retirement savings as a decimal (e.g., 0.50 for 50%)."
)

# Removed Withdrawal Rate input from the UI; withdrawal calculations are now based on Target Monthly Income

# Generate a session ID.
session_id = str(uuid.uuid4())

if st.button("Run Analysis"):
    with st.spinner("Running simulation..."):
        try:
            url = (
                f"http://localhost:8000/analyze?session_id={session_id}"
                f"&birthdate={birthdate}"
                f"&age_model1={int(age_model1)}"
                f"&age_model2={int(age_model2)}"
                f"&fra_benefit={fra_benefit}"
                f"&inflation_rate_input={inflation_rate}"
                f"&investment_return_input={investment_return}"
                f"&filing_status={filing_status}"
                f"&initial_401k_input={initial_401k}"
                f"&other_non_retirement_savings_input={other_non_retirement_savings}"
                f"&target_income_input={target_income}"
                f"&non_retirement_gain_percentage_input={non_retirement_gain_percentage}"
            )
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                st.success("Analysis complete!")
                
                st.subheader("Summary Results")
                df_model1 = pd.DataFrame(data["Model1"])
                df_model2 = pd.DataFrame(data["Model2"])
                
                st.markdown(f"### Claim SS benefits at age {int(age_model1)}")
                st.dataframe(df_model1)
                st.markdown(f"### Claim SS benefits at age {int(age_model2)}")
                st.dataframe(df_model2)
            else:
                st.error(f"Error: {response.status_code}")
        except Exception as e:
            st.error(f"Error connecting to FastAPI backend: {e}")

    file_name = f"social_security_analysis_{session_id}.xlsx"
    try:
        with open(file_name, "rb") as file:
            excel_bytes = file.read()
        st.download_button(
            label="Download Excel Spreadsheet",
            data=excel_bytes,
            file_name=file_name,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        st.info("Excel file not available yet. Please try again in a moment.")