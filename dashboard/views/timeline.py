import streamlit as st
import pandas as pd


def timeline_page(df):

    st.title("📜 Explainable AI Timeline")

    latest = df.iloc[-1]

    timeline = [

        ("📷 Camera Started", latest["timestamp"]),

        ("🙂 Face Detected", latest["timestamp"]),

        (
            f"👀 Attention : {latest['attention_state']}",
            latest["timestamp"]
        ),

        (
            f"😊 Emotion : {latest['emotion']}",
            latest["timestamp"]
        ),

        (
            f"😴 Fatigue : {latest['fatigue']}",
            latest["timestamp"]
        ),

        (
            f"🤖 AI Decision : {latest['action']}",
            latest["timestamp"]
        ),

        (
            "💾 Saved to PostgreSQL",
            latest["timestamp"]
        )

    ]

    for event, time in timeline:

        st.markdown(f"### {event}")

        st.caption(str(time))

        st.markdown("⬇️")