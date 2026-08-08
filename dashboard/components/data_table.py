import streamlit as st


def show_table(df):

    st.subheader("📑 Session Records")

    st.dataframe(

        df,

        width="stretch"

    )

    st.divider()