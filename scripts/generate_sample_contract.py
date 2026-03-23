from reportlab.pdfgen import canvas

c = canvas.Canvas("sample_contract.pdf")
c.drawString(100, 750, "TechNova Offer Letter")
c.drawString(100, 730, "This is a sample contract for testing purposes.")
c.drawString(100, 710, "It contains various clauses that may be risky.")
c.save()