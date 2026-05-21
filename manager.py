import streamlit as st

st.set_page_config(page_title="Manager Dashboard", layout="wide")

st.sidebar.title("Manager Navigation")

view = st.sidebar.radio(
    "Choose a view:",
    [
        "Dashboard",
        "Employee Status Tracker",
        "Performance Log",
        "Business Insights",
        "About This App"
    ]
)

if view == "Dashboard":
    st.title("Manager Dashboard")
    st.write("Overview metrics will go here.")

elif view == "Employee Status Tracker":
    st.title("Employee Status Tracker")
    st.write("Track who is active, unavailable, on job, or completed.")

elif view == "Performance Log":
    st.title("Performance Log")
    st.write("Log employee activity and job performance.")

elif view == "Business Insights":
    st.title("Business Insights")
    st.write("Forecasting, labor productivity, EBITDA-style metrics, and operational KPIs can go here.")

elif view == "About This App":
    st.title("About This App")
    st.write(
        "This app was built to help small businesses track employee activity, "
        "monitor operational performance, and turn daily work data into useful business insights."
    )