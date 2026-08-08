import streamlit as st

from backend.reports.weekly_report import generate_weekly_report
from backend.reports.pdf_report import generate_pdf
from backend.services.audit_service import log_event


st.divider()
if st.button("📄 Generate PDF Report"):

    pdf_file = generate_pdf(report)

    st.write("Generated file:", pdf_file)

    import os

    st.write("Exists:", os.path.exists(pdf_file))

    if os.path.exists(pdf_file):

        st.success("PDF Created Successfully!")

        with open(pdf_file, "rb") as file:

            st.download_button(
                "⬇ Download PDF",
                file,
                file_name="Saathi_Weekly_Report.pdf",
                mime="application/pdf"
            )

    else:

        st.error("PDF was not created.")

        
def weekly_report_page(df):

    st.title("📅 Weekly Report")

    report = generate_weekly_report(df)

    st.metric(
        "Learning Health",
        report["Learning Health Score"]
    )

    st.metric(
        "Average Attention",
        report["Average Attention"]
    )

    st.metric(
        "Emotion",
        report["Emotion"]
    )

    st.metric(
        "Fatigue",
        report["Fatigue"]
    )

    st.subheader("Recommendations")

    for rec in report["Recommendations"]:
        st.success(rec)