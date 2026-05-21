import streamlit as st

st.set_page_config(page_title="CMS App", layout="wide")

if "mode" not in st.session_state:
    st.session_state.mode = "home"

# ---------- HOME PAGE ----------
if st.session_state.mode == "home":
    st.title("CMS Workforce Dashboard")
    st.write("Track employees, monitor performance, and surface business insights.")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Manager Login"):
            st.session_state.mode = "manager"

    with col2:
        if st.button("Employee Login"):
            st.session_state.mode = "employee"

    with col3:
        if st.button("Just Checking Her Out"):
            st.session_state.mode = "demo"

# ---------- MANAGER PLACEHOLDER ----------
elif st.session_state.mode == "manager":
    st.title("Manager Login")
    st.info("Manager portal coming soon.")
    if st.button("Back to Home"):
        st.session_state.mode = "home"

# ---------- EMPLOYEE PLACEHOLDER ----------
elif st.session_state.mode == "employee":
    st.title("Employee Login")
    st.info("Employee portal coming soon.")
    if st.button("Back to Home"):
        st.session_state.mode = "home"

# ---------- DEMO MODE ----------
elif st.session_state.mode == "demo":
    st.sidebar.title("Demo Navigation")

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

    if st.sidebar.button("Back to Home"):
        st.session_state.mode = "home"

    if view == "Dashboard":
        st.title("Dashboard")
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