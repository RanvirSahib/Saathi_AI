import streamlit as st


def show_summary(

    avg_attention,

    emotion,

    fatigue,

    interventions,

    focus_alerts,

    break_alerts

):

    st.subheader("📋 Session Summary")

    st.info(

f"""
📊 Average Attention Score : {avg_attention}

😊 Most Common Emotion : {emotion}

😴 Most Common Fatigue : {fatigue}

🤖 AI Interventions : {interventions}

⚠ Focus Alerts : {focus_alerts}

☕ Break Alerts : {break_alerts}
"""

    )

    st.divider()