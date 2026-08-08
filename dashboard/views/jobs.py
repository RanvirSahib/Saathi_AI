import streamlit as st
import pandas as pd

from backend.services.job_service import fetch_jobs


def jobs_page():

    st.title("⚙ Job Queue Monitor")

    jobs = fetch_jobs()

    if not jobs:

        st.info("No jobs found.")

        return

    data = []

    for job in jobs:

        if job.status == "Completed":

            status = "🟢 Completed"

        elif job.status == "Running":

            status = "🟡 Running"

        elif job.status == "Failed":

            status = "🔴 Failed"

        else:

            status = "⚪ Pending"

        data.append({

            "ID": job.id,

            "Job": job.job_name,

            "Status": status,

            "Created": job.created_at,

            "Completed": job.completed_at

        })

    df = pd.DataFrame(data)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(

        "Total Jobs",

        len(df)

    )

    c2.metric(

        "Completed",

        len(df[df["Status"].str.contains("Completed")])

    )

    c3.metric(

        "Running",

        len(df[df["Status"].str.contains("Running")])

    )

    c4.metric(

        "Failed",

        len(df[df["Status"].str.contains("Failed")])

    )

    st.divider()

    st.dataframe(

        df,

        width="stretch"

    )