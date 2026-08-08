import streamlit as st
import pandas as pd


def audit_page(df):

    st.title("📋 Audit Trail")

    audit_logs = []

    for _, row in df.iterrows():

        audit_logs.append({

            "Timestamp": row["timestamp"],

            "Module": "Camera Analysis",

            "Action": "Session Processed",

            "Status": "SUCCESS"

        })

        audit_logs.append({

            "Timestamp": row["timestamp"],

            "Module": "Attention Detection",

            "Action": row["attention_state"],

            "Status": "SUCCESS"

        })

        audit_logs.append({

            "Timestamp": row["timestamp"],

            "Module": "Emotion Detection",

            "Action": row["emotion"],

            "Status": "SUCCESS"

        })

        audit_logs.append({

            "Timestamp": row["timestamp"],

            "Module": "Fatigue Detection",

            "Action": row["fatigue"],

            "Status": "SUCCESS"

        })

        audit_logs.append({

            "Timestamp": row["timestamp"],

            "Module": "Decision Engine",

            "Action": row["action"],

            "Status": "SUCCESS"

        })

    audit_df = pd.DataFrame(audit_logs)

    st.metric(

        "📑 Total Audit Logs",

        len(audit_df)

    )

    st.divider()

    st.dataframe(

        audit_df,

        width="stretch"

    )