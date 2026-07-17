import streamlit as st

from components.manager_calendar import render_manager_calendar


st.set_page_config(page_title="Employee Portal", layout="wide")

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

    .portal-title {{
        text-align: center;
        color: white;
        font-size: 64px;
        font-weight: 700;
        margin-top: 40px;
        margin-bottom: 60px;
    }}

    .tile-grid {{
        display: grid;
        grid-template-columns: repeat(3, 220px);
        gap: 32px 90px;
        justify-content: center;
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
        color: white !important;
        font-size: 28px;
        font-weight: 700;
        line-height: 1.1;
        text-decoration: none !important;
        padding: 18px;
        box-sizing: border-box;
    }}

    .tile:hover {{
        background-color: #1111a8;
        transform: translateY(-4px);
        transition: all 0.2s ease;
    }}

    .back-link {{
        color: white !important;
        font-size: 20px;
        text-decoration: none !important;
        border: 2px solid white;
        border-radius: 14px;
        padding: 10px 16px;
        display: inline-block;
        margin-bottom: 25px;
    }}

    @media (max-width: 768px) {{
        .portal-title {{
            font-size: 42px;
            margin-top: 20px;
            margin-bottom: 35px;
        }}

        .tile-grid {{
            grid-template-columns: 1fr;
            gap: 24px;
            padding: 0 18px;
        }}

        .tile {{
            width: 100%;
            height: 145px;
            font-size: 26px;
            box-shadow: 6px 6px 0px white;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


view = st.query_params.get("view", "menu")


def employee_menu():
    st.markdown(
        '<div class="portal-title">Lets Get Moving</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="tile-grid">
            <a class="tile" href="?view=current_jobs">Current<br>Jobs</a>
            <a class="tile" href="?view=future_jobs">Future<br>Jobs</a>
            <a class="tile" href="?view=calendar">Calendar</a>
            <a class="tile" href="?view=my_insights">My<br>Insights</a>
            <a class="tile" href="?view=messages">Messages</a>
            <a class="tile" href="?view=report_issue">Report<br>Issue</a>
            <a class="tile" href="?view=pay_hub">Pay<br>Hub</a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def placeholder_page(title, message):
    st.markdown(
        '<a class="back-link" href="?view=menu">'
        "← Back to Employee Portal"
        "</a>",
        unsafe_allow_html=True,
    )

    st.title(title)
    st.info(message)


if view == "menu":
    employee_menu()

elif view == "current_jobs":
    placeholder_page(
        "Current Jobs",
        "Current job details will go here.",
    )

elif view == "future_jobs":
    placeholder_page(
        "Future Jobs",
        "Upcoming assigned jobs will go here.",
    )

elif view == "calendar":
    render_manager_calendar(portal_name="Employee")

elif view == "my_insights":
    placeholder_page(
        "My Insights",
        "Performance stats, completed jobs, ratings, and paperwork trends "
        "will go here.",
    )

elif view == "messages":
    placeholder_page(
        "Messages",
        "Manager updates and job notes will go here.",
    )

elif view == "report_issue":
    placeholder_page(
        "Report Issue",
        "Employees will be able to report delays, damages, or equipment "
        "issues here.",
    )

elif view == "pay_hub":
    placeholder_page(
        "Pay Hub",
        "Hours, bonuses, tips, and overtime snapshots will go here.",
    )

else:
    employee_menu()