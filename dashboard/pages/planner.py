import streamlit as st

from backend.planner.study_planner import generate_study_plan

from backend.services.analytics_service import analytics

data = analytics()

plan = generate_study_plan(

    data["average_attention"],

    data["learning_health"],

    data["emotion"],

    data["fatigue"],

    data["best_hour"]

)