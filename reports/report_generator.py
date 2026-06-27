from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph
import os
from datetime import datetime

REPORT_FOLDER = "reports/generated"

if not os.path.exists(REPORT_FOLDER):
    os.makedirs(REPORT_FOLDER)


def generate_report(data):

    filename = f"{data['username']}_report.pdf"

    filepath = os.path.join(REPORT_FOLDER, filename)

    doc = SimpleDocTemplate(filepath)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b><font size=18>Social Trust AI</font></b>", styles["Title"]))
    story.append(Paragraph("<b>Digital Investigation Report</b>", styles["Heading2"]))

    story.append(Paragraph(
        f"Generated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
        styles["Normal"]
    ))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>Username:</b> {data['username']}", styles["Normal"]))
    story.append(Paragraph(f"<b>Display Name:</b> {data['display_name']}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Trust Analysis</b>", styles["Heading2"]))
    story.append(Paragraph(f"Trust Score: {data['trust_score']}/100", styles["Normal"]))
    story.append(Paragraph(f"Category: {data['category']}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Image Analysis</b>", styles["Heading2"]))
    story.append(Paragraph(data["image_reason"], styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Impersonation Analysis</b>", styles["Heading2"]))
    story.append(Paragraph(f"Similarity: {data['similarity']}%", styles["Normal"]))
    story.append(Paragraph(f"Risk: {data['impersonation_risk']}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Scam Detection</b>", styles["Heading2"]))
    story.append(Paragraph(data["scam_category"], styles["Normal"]))
    story.append(Paragraph(f"Confidence: {data['scam_confidence']}%", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Police Recommendation</b>", styles["Heading2"]))
    story.append(Paragraph(data["recommendation"], styles["Normal"]))
    story.append(Paragraph(f"Priority: {data['priority']}", styles["Normal"]))
    story.append(Paragraph(data["recommendation_reason"], styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(
        "<b>Investigation Summary</b>",
        styles["Heading2"]
    ))

    story.append(
        Paragraph(
            "This profile exhibits suspicious behaviour based on profile characteristics, impersonation analysis, image quality, and scam detection. Manual verification is recommended before taking enforcement action.",
            styles["Normal"]
        )
    )

    doc.build(story)

    return filename