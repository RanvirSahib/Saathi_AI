import streamlit as st

from backend.reports.weekly_report import generate_weekly_report
from backend.services.dashboard_service import get_dashboard_data
from components.metric_cards import metric_card

metric_card(
    "Average Attention",
    91
)

def weekly_report_page():

    st.title("📅 Weekly Report")

    df = get_dashboard_data()

    report = generate_weekly_report(df)

    st.metric(
        "Learning Health",
        report["Learning Health Score"]
    )

    st.metric(
        "Average Attention",
        report["Average Attention"]
    )