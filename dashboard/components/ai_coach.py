import streamlit as st


def show_ai_coach(latest):

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

    st.divider()