from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)
from reportlab.lib.units import inch


def create_report(
    filename,
    ats_result,
    career_result,
    coach_result,
):

    pdf_file = "CareerPilot_Report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    story = []

    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b><font size=20>CareerPilot AI</font></b>",
            styles["Title"],
        )
    )

    story.append(
        Paragraph(
            "Resume Analysis Report",
            styles["Heading2"],
        )
    )

    story.append(Spacer(1, 0.3 * inch))

    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b>Resume</b>",
            styles["Heading2"],
        )
    )

    story.append(
        Paragraph(
            filename,
            styles["BodyText"],
        )
    )

    story.append(Spacer(1, 0.2 * inch))

    # -------------------------------------------------

    if ats_result:

        story.append(
            Paragraph(
                "<b>ATS Score</b>",
                styles["Heading2"],
            )
        )

        story.append(
            Paragraph(
                str(ats_result["ats_score"]) + "%",
                styles["BodyText"],
            )
        )

        story.append(Spacer(1, 0.1 * inch))

        story.append(
            Paragraph(
                "<b>Matched Skills</b>",
                styles["Heading3"],
            )
        )

        for skill in ats_result["matched_skills"]:

            story.append(
                Paragraph(
                    "• " + skill,
                    styles["BodyText"],
                )
            )

        story.append(Spacer(1, 0.15 * inch))

        story.append(
            Paragraph(
                "<b>Missing Skills</b>",
                styles["Heading3"],
            )
        )

        for skill in ats_result["missing_skills"]:

            story.append(
                Paragraph(
                    "• " + skill,
                    styles["BodyText"],
                )
            )

    story.append(Spacer(1, 0.25 * inch))

    # -------------------------------------------------

    if career_result:

        story.append(
            Paragraph(
                "<b>Career Recommendations</b>",
                styles["Heading2"],
            )
        )

        for role in career_result["recommended_roles"]:

            story.append(

                Paragraph(

                    f"{role['role']} ({role['match_percentage']}%)",

                    styles["BodyText"],

                )

            )

    story.append(Spacer(1, 0.25 * inch))

    # -------------------------------------------------

    if coach_result:

        story.append(
            Paragraph(
                "<b>AI Career Coach Advice</b>",
                styles["Heading2"],
            )
        )

        story.append(
            Paragraph(
                coach_result["advice"].replace("\n", "<br/>"),
                styles["BodyText"],
            )
        )

    doc.build(story)

    return pdf_file