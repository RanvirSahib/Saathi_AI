import streamlit as st
import pandas as pd
import plotly.express as px


def show_charts(df):

    df = df.copy()

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # -------------------------------
    # Attention Timeline
    # -------------------------------

    st.subheader("📈 Attention Score Timeline")

    fig_attention = px.line(

        df,

        x="timestamp",

        y="attention_score",

        markers=True,

        title="Attention Score"

    )

    st.plotly_chart(

        fig_attention,

        width="stretch"

    )

    # -------------------------------
    # Emotion Distribution
    # -------------------------------

    st.subheader("😊 Emotion Distribution")

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

        width="stretch"

    )

    # -------------------------------
    # Fatigue Distribution
    # -------------------------------

    st.subheader("😴 Fatigue Distribution")

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

        width="stretch"

    )

    # -------------------------------
    # AI Actions
    # -------------------------------

    st.subheader("🤖 AI Action Distribution")

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

        width="stretch"

    )