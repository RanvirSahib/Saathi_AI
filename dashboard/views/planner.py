import streamlit as st

from backend.services.analytics_service import analytics
from backend.planner.study_planner import generate_study_plan


def planner_page(df):

    st.title("🤖 AI Study Planner")

    if st.button("Generate Study Plan"):

        data = analytics()

        plan = generate_study_plan(

            data["average_attention"],
            data["learning_health"],
            data["emotion"],
            data["fatigue"],
            data["best_hour"]

        )

        st.success(plan)