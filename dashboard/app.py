import streamlit as st

from pages.dashboard import dashboard_page
from pages.analytics import analytics_page
from pages.weekly_report import weekly_report_page
from pages.planner import planner_page

st.set_page_config(
    page_title="Saathi AI",
    layout="wide"
)

st.sidebar.title("🧠 Saathi AI")

page = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Dashboard",

        "📊 Analytics",

        "📅 Weekly Report",

        "🤖 AI Planner"

    ]

)

if page == "🏠 Dashboard":

    dashboard_page()

elif page == "📊 Analytics":

    analytics_page()

elif page == "📅 Weekly Report":

    weekly_report_page()

elif page == "🤖 AI Planner":

    planner_page()

def load_css():

    with open("dashboard/assets/styles.css") as f:

        st.markdown(

            f"<style>{f.read()}</style>",

            unsafe_allow_html=True

        )

load_css()