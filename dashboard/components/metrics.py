import streamlit as st


def show_metrics(

    avg_attention,
    total_records,
    focus_alerts,
    break_alerts,
    emotion,
    fatigue,
    interventions,
    focus_score

):

    st.subheader("📊 Performance Metrics")

    row1 = st.columns(4)

    row1[0].metric(
        "🎯 Focus Score",
        f"{focus_score}/100"
    )

    row1[1].metric(
        "📈 Avg Attention",
        avg_attention
    )

    row1[2].metric(
        "⚠ Focus Alerts",
        focus_alerts
    )

    row1[3].metric(
        "☕ Break Alerts",
        break_alerts
    )

    row2 = st.columns(3)

    row2[0].metric(
        "😊 Emotion",
        emotion
    )

    row2[1].metric(
        "😴 Fatigue",
        fatigue
    )

    row2[2].metric(
        "🤖 AI Actions",
        interventions
    )

    st.divider()