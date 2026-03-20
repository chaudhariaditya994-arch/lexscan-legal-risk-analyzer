from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "sample_contracts"
OUTPUT_PATH = OUTPUT_DIR / "TechNova_Offer_Letter.pdf"

CLAUSES = [
    "Probation: The first 12 months of employment shall be treated as probation. During probation, the Company may terminate employment instantly without notice or severance.",
    "Work Hours: The Employee shall remain available for 57.5 hours per week as operationally required, and no overtime pay, compensatory leave, or additional allowance shall be payable.",
    "Intellectual Property: All ideas, inventions, code, notes, designs, and work product conceived during employment shall belong to the Company, including work created on personal devices and during personal time.",
    "Non-Compete: For 36 months after separation, the Employee shall not directly or indirectly engage with any competing enterprise worldwide. Each breach will attract liquidated damages of Rs. 25,00,000.",
    "Termination Notice: The Company may terminate this Agreement with 30 days notice. The Employee must provide 90 days notice, failing which an amount equal to 3 months salary shall be payable.",
    "Employment Bond: The Employee agrees to an initial 24 month employment bond that shall automatically renew for a further 24 month term unless expressly waived by the Company in writing.",
    "Dispute Resolution: All disputes shall be referred to mandatory arbitration only. No party may approach any court, and arbitration fees shall be equally split irrespective of outcome.",
    "Salary Deductions: The Employee irrevocably authorizes the Company to make unlimited salary deductions for losses, penalties, training costs, claims, advances, or any amount deemed payable by the Company.",
    "Confidentiality: Confidentiality obligations shall continue forever and without limitation in duration regardless of the nature of the information.",
    "Social Media: The Employee shall not publish, repost, endorse, or update any professional or personal social media content, including LinkedIn changes, without prior HR approval.",
]


def build_offer_letter() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(OUTPUT_PATH), pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=15 * mm, bottomMargin=15 * mm)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="SmallCaps", parent=styles["BodyText"], fontSize=9, textColor=colors.HexColor("#475569")))
    story = [
        Paragraph("<b>TechNova Solutions Pvt. Ltd.</b>", styles["Title"]),
        Paragraph("Senapati Bapat Road, Pune, Maharashtra 411016", styles["SmallCaps"]),
        Spacer(1, 8),
        Paragraph("<b>Offer Letter</b>", styles["Heading1"]),
        Paragraph("Date: 20 March 2026", styles["BodyText"]),
        Spacer(1, 10),
        Paragraph("Candidate: <b>Aditya Sharma</b>", styles["BodyText"]),
        Paragraph("Position: Senior Software Engineer", styles["BodyText"]),
        Paragraph("Location: Pune", styles["BodyText"]),
        Spacer(1, 14),
        Paragraph("Dear Aditya Sharma,", styles["BodyText"]),
        Paragraph("We are pleased to offer you employment with TechNova Solutions Pvt. Ltd. on the following terms and conditions.", styles["BodyText"]),
        Spacer(1, 14),
    ]

    compensation_table = Table(
        [
            ["Component", "Annual Amount (INR)"],
            ["Base Salary", "18,00,000"],
            ["Joining Bonus", "1,50,000"],
            ["Retention Bonus", "2,00,000"],
            ["Total Target Compensation", "21,50,000"],
        ],
        colWidths=[85 * mm, 65 * mm],
    )
    compensation_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dbeafe")),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#94a3b8")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("PADDING", (0, 0), (-1, -1), 6),
    ]))
    story.extend([Paragraph("<b>Compensation</b>", styles["Heading2"]), compensation_table, Spacer(1, 16)])

    story.append(Paragraph("<b>Key Terms</b>", styles["Heading2"]))
    for index, clause in enumerate(CLAUSES, start=1):
        story.append(Paragraph(f"{index}. {clause}", styles["BodyText"]))
        story.append(Spacer(1, 6))

    story.extend([
        Spacer(1, 16),
        Paragraph("Please sign below to confirm your acceptance of this offer and all terms above.", styles["BodyText"]),
        Spacer(1, 24),
        Paragraph("For TechNova Solutions Pvt. Ltd.", styles["BodyText"]),
        Spacer(1, 20),
        Paragraph("______________________________", styles["BodyText"]),
        Paragraph("Authorized Signatory", styles["BodyText"]),
        Spacer(1, 20),
        Paragraph("Accepted by Aditya Sharma", styles["BodyText"]),
        Spacer(1, 20),
        Paragraph("______________________________", styles["BodyText"]),
        Paragraph("Signature", styles["BodyText"]),
    ])

    doc.build(story)
    print(f"Generated sample contract at {OUTPUT_PATH}")


if __name__ == "__main__":
    build_offer_letter()
