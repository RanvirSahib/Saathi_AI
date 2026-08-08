from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(report, filename="weekly_report.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("<b>Saathi AI Weekly Report</b>", styles["Title"]))

    elements.append(Paragraph(f"Learning Health Score: {report['Learning Health Score']}", styles["BodyText"]))
    elements.append(Paragraph(f"Average Attention: {report['Average Attention']}", styles["BodyText"]))
    elements.append(Paragraph(f"Emotion: {report['Emotion']}", styles["BodyText"]))
    elements.append(Paragraph(f"Fatigue: {report['Fatigue']}", styles["BodyText"]))
    elements.append(Paragraph(f"Focus Alerts: {report['Focus Alerts']}", styles["BodyText"]))
    elements.append(Paragraph(f"Break Alerts: {report['Break Alerts']}", styles["BodyText"]))

    elements.append(Paragraph("<br/><b>Recommendations</b>", styles["Heading2"]))

    for rec in report["Recommendations"]:
        elements.append(Paragraph(f"• {rec}", styles["BodyText"]))

    doc.build(elements)

    return filename