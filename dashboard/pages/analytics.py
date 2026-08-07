import streamlit as st
from components.metric_cards import metric_card

metric_card(
    "Average Attention",
    91
)

def analytics_page():

    st.title("📊 Analytics")

    st.info("Analytics coming soon.")