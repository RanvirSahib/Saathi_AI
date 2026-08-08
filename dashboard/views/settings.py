import streamlit as st


def settings_page():

    st.title("⚙ Settings")

    st.subheader("Dashboard")

    dark_mode = st.toggle(
        "Dark Mode",
        value=False
    )

    auto_refresh = st.toggle(
        "Auto Refresh Dashboard",
        value=True
    )

    st.divider()

    st.subheader("Export")

    st.button("📄 Export Weekly Report")

    st.button("📊 Export Analytics")

    st.button("📋 Export Audit Logs")

    st.divider()

    st.subheader("About")

    st.info(
        """
Saathi AI Version 2.0

OpenCV

MediaPipe

EfficientNet-B0

Gemini AI

PostgreSQL
"""
    )