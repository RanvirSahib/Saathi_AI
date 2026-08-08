import streamlit as st


def validation_page(df):

    st.title("🛡 Validation Dashboard")

    valid_sessions = len(df[df["attention_score"] >= 40])

    invalid_sessions = len(df[df["attention_score"] < 40])

    safety_flags = len(
        df[
            (df["fatigue"] != "Normal") |
            (df["action"] == "BREAK")
        ]
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "✅ Valid Sessions",
        valid_sessions
    )

    c2.metric(
        "❌ Invalid Sessions",
        invalid_sessions
    )

    c3.metric(
        "⚠ Safety Flags",
        safety_flags
    )

    st.divider()

    validation_df = df.copy()

    validation_df["Validation"] = validation_df[
        "attention_score"
    ].apply(

        lambda x:
        "PASS"
        if x >= 40
        else "FAIL"

    )

    validation_df["Reason"] = validation_df.apply(

        lambda row:
        "Low Attention"
        if row["attention_score"] < 40
        else "Normal",

        axis=1

    )

    st.dataframe(

        validation_df[
            [
                "timestamp",
                "attention_score",
                "Validation",
                "Reason"
            ]
        ],

        width="stretch"

    )