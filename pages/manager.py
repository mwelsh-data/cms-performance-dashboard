import streamlit as st
import pandas as pd
from supabase import create_client
from dotenv import load_dotenv
import os

st.set_page_config(page_title="Manager Portal", layout="wide")

CMS_BLUE = "#000080"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {CMS_BLUE};
        color: white;
    }}

    h1, h2, h3, p, label, div {{
        font-family: "Cresta", Georgia, serif;
    }}

    .manager-title {{
        text-align: center;
        color: white;
        font-size: 64px;
        font-weight: 700;
        margin-top: 30px;
        margin-bottom: 10px;
    }}

    .manager-subtitle {{
        text-align: center;
        color: white;
        font-size: 34px;
        margin-bottom: 50px;
    }}

    .tile-grid {{
        display: grid;
        grid-template-columns: repeat(3, 220px);
        gap: 32px 90px;
        justify-content: center;
        align-items: center;
    }}

    .tile {{
        width: 220px;
        height: 220px;
        background-color: {CMS_BLUE};
        border: 4px solid white;
        border-radius: 34px;
        box-shadow: 8px 8px 0px white;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        color: white;
        font-size: 28px;
        font-weight: 700;
        line-height: 1.1;
        text-decoration: none;
        padding: 18px;
        box-sizing: border-box;
    }}

    .tile:hover {{
        background-color: #1111a8;
        transform: translateY(-4px);
        transition: all 0.2s ease;
        color: white;
        text-decoration: none;
    }}

    .back-link {{
        color: white;
        font-size: 20px;
        text-decoration: none;
        border: 2px solid white;
        border-radius: 14px;
        padding: 10px 16px;
        display: inline-block;
        margin-bottom: 25px;
    }}

    .back-link:hover {{
        background-color: white;
        color: {CMS_BLUE};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

view = st.query_params.get("view", "menu")


def manager_menu():
    st.markdown('<div class="manager-title">Hello Boss Man</div>', unsafe_allow_html=True)
    st.markdown('<div class="manager-subtitle">What are we moving today?</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="tile-grid">
            <a class="tile" href="?view=employee_tracking">Employee<br>Tracking</a>
            <a class="tile" href="?view=scheduling">Scheduling</a>
            <a class="tile" href="?view=calendar">Calendar</a>
            <a class="tile" href="?view=job_board">Job<br>Board</a>
            <a class="tile" href="?view=crew_management">Crew<br>Management</a>
            <a class="tile" href="?view=insights">Insights</a>
            <a class="tile" href="?view=claims">Claims</a>
            <a class="tile" href="?view=customer_feedback">Customer<br>Feedback</a>
            <a class="tile" href="?view=fleet">Fleet /<br>Equipment</a>
        </div>
        """,
        unsafe_allow_html=True
    )


def employee_tracking():
    st.markdown('<a class="back-link" href="?view=menu">← Back to Manager Portal</a>', unsafe_allow_html=True)

    st.title("Employee Tracking")

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

    response = supabase.table("job_performance").select("*").execute()
    df = pd.DataFrame(response.data)

    if not df.empty:
        st.subheader("Performance Records")
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No performance records yet.")


def placeholder_page(title):
    st.markdown('<a class="back-link" href="?view=menu">← Back to Manager Portal</a>', unsafe_allow_html=True)
    st.title(title)
    st.info(f"{title} coming soon.")


if view == "menu":
    manager_menu()
elif view == "employee_tracking":
    employee_tracking()
elif view == "scheduling":
    placeholder_page("Scheduling")
elif view == "calendar":
    placeholder_page("Calendar")
elif view == "job_board":
    placeholder_page("Job Board")
elif view == "crew_management":
    placeholder_page("Crew Management")
elif view == "insights":
    placeholder_page("Insights")
elif view == "claims":
    placeholder_page("Claims")
elif view == "customer_feedback":
    placeholder_page("Customer Feedback")
elif view == "fleet":
    placeholder_page("Fleet / Equipment")
else:
    manager_menu()