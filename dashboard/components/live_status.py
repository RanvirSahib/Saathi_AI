import streamlit as st


def show_live_status(latest):

    st.subheader("🟢 Live Status")

    col1, col2 = st.columns(2)

    with col1:

        st.success(
            f"🎯 Attention : {latest['attention_state']}"
        )

        st.info(
            f"😊 Emotion : {latest['emotion']}"
        )

    with col2:

        st.warning(
            f"😴 Fatigue : {latest['fatigue']}"
        )

        st.error(
            f"🤖 Action : {latest['action']}"
        )

    st.divider()