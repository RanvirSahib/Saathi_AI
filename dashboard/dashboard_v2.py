import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

import streamlit as st

st.set_page_config(
    page_title="Saathi Dashboard",
    page_icon="dashboard/assets/logo.png",
    layout="wide"
)


from backend.services.dashboard_service import get_dashboard_data

from dashboard.views.dashboard import dashboard_page
from dashboard.views.analytics import analytics_page
from dashboard.views.weekly_report import weekly_report_page
from dashboard.views.planner import planner_page
from dashboard.views.validation import validation_page
from dashboard.views.audit import audit_page
from dashboard.views.jobs import jobs_page
from dashboard.views.timeline import timeline_page
from dashboard.views.settings import settings_page

st.sidebar.title("🧠 Saathi")



page = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Dashboard",

        "📊 Analytics",

        "📅 Weekly Report",

        "🤖 AI Planner",

        "🛡 Validation",

        "📋 Audit",

        "⚙ Job Queue",

        "📜 Timeline",

        "⚙ Settings"

    ]

)

df = get_dashboard_data()

if page == "🏠 Dashboard":

    dashboard_page(df)

elif page == "📊 Analytics":

    analytics_page(df)

elif page == "📅 Weekly Report":

    weekly_report_page(df)

elif page == "🤖 AI Planner":

    planner_page(df)

elif page == "🛡 Validation":

    validation_page(df)

elif page == "📋 Audit":

    audit_page(df)

elif page == "⚙ Job Queue":

    jobs_page()

elif page == "📜 Timeline":

    timeline_page(df)

elif page == "⚙ Settings":

    settings_page()