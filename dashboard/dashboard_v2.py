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
import pandas as pd
import plotly.express as px

from backend.services.dashboard_service import get_dashboard_data
# from backend.planner.study_planner import generate_study_plan
# from backend.services.planner_service import (
#     save_plan,
#     get_latest_plan
# )
#---------------------
#SlideBar Navigation
#---------------------

st.sidebar.title("🧠 Saathi")

page = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Dashboard",

        "📊 Analytics",

        "📅 Weekly Report",

        "🤖 AI Planner",

        "⚙ Settings"

    ]

)
st.set_page_config(
    page_title="Saathi Dashboard",
    layout="wide"
)


st.title("🧠 Saathi AI Dashboard")

st.caption(
    "AI-Powered Student Learning Analytics Platform"
)

st.divider()


df = get_dashboard_data()

#-------------------------------
#LIVE STATUS CARD
#--------------------------------

latest = df.iloc[-1]

st.subheader("🟢 Live Status")

col1, col2 = st.columns(2)

with col1:

    st.success(
        f"Attention : {latest['attention_state']}"
    )

    st.info(
        f"Emotion : {latest['emotion']}"
    )

with col2:

    st.warning(
        f"Fatigue : {latest['fatigue']}"
    )

    st.error(
        f"Action : {latest['action']}"
    )

st.divider()

# ---------------------------------
# ADVANCED METRICS
# ---------------------------------

avg_attention = round(
    df["attention_score"].mean(),
    2
)

total_records = len(df)

focus_alerts = len(
    df[df["action"] == "FOCUS"]
)

break_alerts = len(
    df[df["action"] == "BREAK"]
)

most_common_emotion = (
    df["emotion"]
    .mode()[0]
)

most_common_fatigue = (
    df["fatigue"]
    .mode()[0]
)

ai_interventions = len(
    df[df["action"] != "NONE"]
)

#----------------------
# FOCUS SCORE
#---------------------

focus_score = round(

    avg_attention * 0.7 +

    (100 if most_common_emotion in ["happy","neutral"] else 70) * 0.2 +

    (100 if most_common_fatigue == "Normal" else 60) * 0.1,

    2

)

# ---------------------------------
# METRIC CARDS
# ---------------------------------

col1, col2, col3, col4 = st.columns(4)

col8 = st.columns(1)[0]

col8.metric(

    "🎯 Focus Score",

    f"{focus_score}/100"

)

col1.metric(
    "Average Attention",
    avg_attention
)

col2.metric(
    "Records",
    total_records
)

col3.metric(
    "Focus Alerts",
    focus_alerts
)

col4.metric(
    "Break Alerts",
    break_alerts
)

col5, col6, col7 = st.columns(3)

col5.metric(
    "Common Emotion",
    most_common_emotion
)

col6.metric(
    "Common Fatigue",
    most_common_fatigue
)

col7.metric(
    "AI Interventions",
    ai_interventions
)
# ---------------------------------
# ATTENTION GRAPH
# ---------------------------------

st.subheader(
    "Attention Score Timeline"
)

df["timestamp"] = pd.to_datetime(
    df["timestamp"]
)


fig_attention = px.line(
    df,
    x="timestamp",
    y="attention_score",
    title="Attention Score Timeline",
    markers=True
)


st.plotly_chart(
    fig_attention,
    use_container_width=True
)

# ---------------------------------
# EMOTION DISTRIBUTION
# ---------------------------------

st.subheader(
    "Emotion Distribution"
)

emotion_counts = (
    df["emotion"]
    .value_counts()
    .reset_index()
)

emotion_counts.columns = [
    "emotion",
    "count"
]

fig_emotion = px.pie(
    emotion_counts,
    names="emotion",
    values="count"
)

st.plotly_chart(
    fig_emotion,
    use_container_width=True
)

# ---------------------------------
# FATIGUE DISTRIBUTION
# ---------------------------------

st.subheader(
    "Fatigue States"
)

fatigue_counts = (
    df["fatigue"]
    .value_counts()
    .reset_index()
)

fatigue_counts.columns = [
    "fatigue",
    "count"
]

fig_fatigue = px.bar(
    fatigue_counts,
    x="fatigue",
    y="count"
)

st.plotly_chart(
    fig_fatigue,
    use_container_width=True
)

# ---------------------------------
# ACTION DISTRIBUTION
# ---------------------------------

st.subheader(
    "AI Intervention Distribution"
)

action_counts = (
    df["action"]
    .value_counts()
    .reset_index()
)

action_counts.columns = [
    "action",
    "count"
]

fig_action = px.bar(
    action_counts,
    x="action",
    y="count",
    title="AI Actions"
)

st.plotly_chart(
    fig_action,
    use_container_width=True
)



st.subheader("🤖 AI Coach")

if latest["action"] == "FOCUS":

    recommendation = """
Try minimizing distractions.
Study in 25-minute focus sessions.
"""

elif latest["action"] == "BREAK":

    recommendation = """
Take a 10-minute break.
Stretch and drink some water.
"""

else:

    recommendation = """
Excellent work!
Keep maintaining your current pace.
"""

st.info(recommendation)

# ---------------------------------
# SESSION SUMMARY
# ---------------------------------

st.subheader(
    "Session Summary"
)

st.info(
    f"""
📊 Average Attention Score: {avg_attention}

😊 Most Common Emotion: {most_common_emotion}

😴 Most Common Fatigue State: {most_common_fatigue}

🤖 Total AI Interventions: {ai_interventions}

⚠️ Focus Alerts: {focus_alerts}

☕ Break Alerts: {break_alerts}
"""
)


# ---------------------------------
# DATA TABLE
# ---------------------------------

st.subheader(
    "Session Records"
)

st.dataframe(df)


# ---------------------------------
# WEEKLY REPORT 
# ---------------------------------


st.subheader("📅 Weekly Report")

if st.button("Generate Weekly Report"):

    st.success(
        "Weekly Report feature coming soon."
    )

#------------------
#FOOTER
#------------------
st.divider()

st.caption(

    "Saathi AI • Version 2.0 • Powered by OpenCV, MediaPipe, EfficientNet-B0, Gemini AI and PostgreSQL"

)


if page == "📅 Weekly Report":
    from backend.reports.weekly_report import (
        generate_weekly_report
    )

    report = generate_weekly_report(df)

    st.title("📅 Weekly Report")

    st.metric(
        "Learning Health",
        report["Learning Health Score"]
    )

    st.metric(
        "Average Attention",
        report["Average Attention"]
    )

    st.metric(
        "Emotion",
        report["Emotion"]
    )

    st.metric(
        "Fatigue",
        report["Fatigue"]
    )

    st.metric(
        "Focus Alerts",
        report["Focus Alerts"]
    )

    st.metric(
        "Break Alerts",
        report["Break Alerts"]
    )

    st.subheader("🤖 AI Recommendation")

    for rec in report["Recommendations"]:

        st.success(rec)

elif page == "🤖 AI Planner":
    st.title("🤖 AI Study Planner")
    st.info("Coming Soon")


# latest = get_latest_plan()

# if latest:

#     st.subheader("Latest Plan")

#     st.info(latest.schedule)