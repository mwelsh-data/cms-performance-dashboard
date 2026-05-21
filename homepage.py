import streamlit as st

st.set_page_config(page_title="CMS Internal Portal", layout="wide")

CMS_BLUE = "#000080"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {CMS_BLUE};
    }}

    section.main > div {{
        padding-top: 0rem;
    }}

    .logo-center {{
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin-top: 30px;
        margin-bottom: 20px;
    }}

    .welcome {{
        text-align: center;
        color: white;
        font-family: Georgia, serif;
        font-size: 60px;
        font-weight: 700;
        margin-bottom: 60px;
    }}

    div.stButton {{
        display: flex;
        justify-content: center;
    }}

    div.stButton > button {{
        width: 360px !important;
        height: 280px !important;
        background-color: {CMS_BLUE} !important;
        color: white !important;
        border-radius: 48px !important;
        border: 4px solid white !important;
        font-size: 64px !important;
        font-weight: 700 !important;
        line-height: 1 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.25);
    }}

    div.stButton > button:hover {{
        background-color: #1111a8 !important;
        transform: translateY(-6px);
        transition: all 0.2s ease;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="logo-center">', unsafe_allow_html=True)
st.image("image(246).png", width=420)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="welcome">Welcome Home</div>', unsafe_allow_html=True)

spacer1, col1, col2, spacer2 = st.columns([1, 2, 2, 1])

with col1:
    if st.button("Manager"):
        st.switch_page("manager.py")

with col2:
    if st.button("Employee"):
        st.switch_page("employee.py")