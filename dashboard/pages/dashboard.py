import streamlit as st

from backend.services.dashboard_service import get_dashboard_data

from components.metric_cards import metric_card

metric_card(
    "Average Attention",
    91
)

def dashboard_page():

    st.title("🏠 Dashboard")

    df = get_dashboard_data()

    st.write(df.head())