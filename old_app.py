import streamlit as st
import pandas as pd
from supabase import create_client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Connect to Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("CMS Employee Performance Dashboard")

# Input form
with st.form("employee_form"):
    employee_name = st.text_input("Employee Name")
    jobs_completed = st.number_input("Jobs Completed", min_value=0, step=1)
    customer_rating = st.number_input("Customer Rating", min_value=0.0, max_value=5.0, step=0.1)
    late_arrival = st.checkbox("Late Arrival")
    damage_claim = st.checkbox("Damage Claim")
    paperwork_complete = st.checkbox("Paperwork Complete")
    notes = st.text_area("Notes")

    submitted = st.form_submit_button("Submit")

    if submitted:
        data = {
            "employee_name": employee_name,
            "jobs_completed": jobs_completed,
            "customer_rating": customer_rating,
            "late_arrival": late_arrival,
            "damage_claim": damage_claim,
            "paperwork_complete": paperwork_complete,
            "notes": notes
        }

        supabase.table("job_performance").insert(data).execute()
        st.success("Performance record added!")

# Load data
response = supabase.table("job_performance").select("*").execute()
df = pd.DataFrame(response.data)

if not df.empty:
    st.subheader("Performance Records")
    st.dataframe(df)