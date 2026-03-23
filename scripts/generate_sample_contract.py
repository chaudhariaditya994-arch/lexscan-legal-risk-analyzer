from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

def generate_sample_contract():
    doc = SimpleDocTemplate("sample_contracts/TechNova_Offer_Letter.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Letterhead
    story.append(Paragraph("TechNova Solutions Pvt. Ltd.", styles['Heading1']))
    story.append(Paragraph("123 Innovation Drive, Pune, Maharashtra 411001", styles['Normal']))
    story.append(Paragraph("Phone: +91-20-1234-5678 | Email: hr@technova.com", styles['Normal']))
    story.append(Spacer(1, 12))

    # Date
    story.append(Paragraph("March 23, 2026", styles['Normal']))
    story.append(Spacer(1, 12))

    # Candidate Address
    story.append(Paragraph("Aditya Sharma", styles['Normal']))
    story.append(Paragraph("456 Residency Apartments", styles['Normal']))
    story.append(Paragraph("Pune, Maharashtra 411002", styles['Normal']))
    story.append(Spacer(1, 12))

    # Subject
    story.append(Paragraph("Subject: Offer Letter for Software Engineer Position", styles['Heading2']))
    story.append(Spacer(1, 12))

    # Salutation
    story.append(Paragraph("Dear Aditya Sharma,", styles['Normal']))
    story.append(Spacer(1, 12))

    # Introduction
    intro = """
    We are pleased to offer you the position of Software Engineer at TechNova Solutions Pvt. Ltd. 
    This offer is contingent upon successful completion of background verification and reference checks.
    """
    story.append(Paragraph(intro, styles['Normal']))
    story.append(Spacer(1, 12))

    # Compensation
    story.append(Paragraph("Compensation Package:", styles['Heading3']))
    data = [
        ['Component', 'Amount'],
        ['Basic Salary', '₹8,00,000 per annum'],
        ['HRA', '₹3,20,000 per annum'],
        ['Conveyance Allowance', '₹19,200 per annum'],
        ['LTA', '₹1,00,000 per annum'],
        ['Total CTC', '₹12,39,200 per annum']
    ]
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(table)
    story.append(Spacer(1, 12))

    # Risky Clauses
    clauses = [
        "1. Probation Period: You will be on probation for 12 months. During this period, your employment can be terminated instantly without any notice or reason.",
        "2. Working Hours: You are expected to work 57.5 hours per week. No overtime pay will be provided for additional hours worked.",
        "3. Intellectual Property: You assign all intellectual property rights, including work done on personal devices and during personal time, to the company.",
        "4. Non-Compete: You agree not to work for any competitor within 36 months of leaving the company, globally. Breach penalty is ₹25 lakhs per violation.",
        "5. Termination: Company can terminate with 30 days notice. You must give 90 days notice. Early termination by you incurs 3-month salary penalty.",
        "6. Employment Bond: This employment agreement auto-renews for 24 months unless terminated with 6 months notice.",
        "7. Dispute Resolution: All disputes must be resolved through mandatory arbitration. No access to courts. Arbitration costs split equally.",
        "8. Salary Deductions: Company can deduct unlimited amounts from your salary for any reason deemed necessary.",
        "9. Confidentiality: Confidentiality obligations continue indefinitely, even after employment ends.",
        "10. Social Media: You cannot post on social media, including LinkedIn, without prior HR approval. Violation leads to immediate termination."
    ]

    story.append(Paragraph("Terms and Conditions:", styles['Heading3']))
    for clause in clauses:
        story.append(Paragraph(clause, styles['Normal']))
        story.append(Spacer(1, 6))

    # Closing
    story.append(Paragraph("We look forward to your joining TechNova Solutions.", styles['Normal']))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Sincerely,", styles['Normal']))
    story.append(Spacer(1, 24))
    story.append(Paragraph("HR Manager", styles['Normal']))
    story.append(Paragraph("TechNova Solutions Pvt. Ltd.", styles['Normal']))

    doc.build(story)

if __name__ == "__main__":
    generate_sample_contract()