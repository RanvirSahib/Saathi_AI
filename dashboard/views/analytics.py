import streamlit as st
import pandas as pd
import plotly.express as px


def analytics_page(df):

    st.title("📊 Analytics")

    avg_attention = round(df["attention_score"].mean(), 2)

    st.metric(
        "Average Attention",
        avg_attention
    )

    df = df.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    fig = px.line(
        df,
        x="timestamp",
        y="attention_score",
        title="Attention Trend",
        markers=True
    )

    st.plotly_chart(
        fig,
        width="stretch",
        key="analytics_attention"
    )