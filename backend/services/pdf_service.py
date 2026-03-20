from __future__ import annotations

from io import BytesIO
from typing import Any

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


def build_report_pdf(analysis: dict[str, Any]) -> bytes:
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    story = [
        Paragraph("LEXSCAN Legal Risk Report", styles["Title"]),
        Spacer(1, 12),
        Paragraph(f"Document: {analysis['documentTitle']}", styles["Heading2"]),
        Paragraph(f"Overall risk: {analysis['overallRisk']} ({analysis['overallRiskScore']}/100)", styles["BodyText"]),
        Spacer(1, 12),
        Paragraph(analysis["executiveSummary"], styles["BodyText"]),
        Spacer(1, 18),
    ]

    for clause in analysis.get("clauses", []):
        table = Table([
            ["Clause", clause["title"]],
            ["Category", clause["category"]],
            ["Risk", f"{clause['risk']} ({clause['score']}/100)"],
            ["Text", clause["clauseText"]],
            ["Why it matters", clause["explanation"]],
            ["Recommendation", clause["recommendation"]],
        ], colWidths=[110, 360])
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#e0f2fe")),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ]))
        story.extend([table, Spacer(1, 16)])

    doc.build(story)
    return buffer.getvalue()
