import streamlit as st

from dashboard.components.live_status import show_live_status
from dashboard.components.metrics import show_metrics
from dashboard.components.charts import show_charts
from dashboard.components.ai_coach import show_ai_coach
from dashboard.components.summary import show_summary
from dashboard.components.data_table import show_table
from dashboard.components.footer import show_footer

col1, col2 = st.columns([1,4])

with col1:
    st.image(
        "dashboard/assets/logo.png",
        width=110
    )

with col2:
    st.title("Saathi AI")
    st.caption(
        "AI Powered Student Learning Analytics Platform"
    )

def dashboard_page(df):

    st.title("🧠 Saathi AI Dashboard")

    st.caption(
        "AI-Powered Student Learning Analytics Platform"
    )

    st.divider()

    latest = df.iloc[-1]

    show_live_status(latest)

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

    focus_score = round(

        avg_attention * 0.7 +

        (100 if most_common_emotion in ["happy", "neutral"] else 70) * 0.2 +

        (100 if most_common_fatigue == "Normal" else 60) * 0.1,

        2

    )

    show_metrics(

        avg_attention,

        total_records,

        focus_alerts,

        break_alerts,

        most_common_emotion,

        most_common_fatigue,

        ai_interventions,

        focus_score

    )

    show_charts(df)

    show_ai_coach(latest)

    show_summary(

        avg_attention,

        most_common_emotion,

        most_common_fatigue,

        ai_interventions,

        focus_alerts,

        break_alerts

    )

    show_table(df)

    show_footer()