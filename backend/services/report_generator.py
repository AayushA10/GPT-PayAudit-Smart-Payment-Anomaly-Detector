from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_pdf_report(filename: str, summary: str, anomalies: list):
    path = f"data/{filename}_report.pdf"
    c = canvas.Canvas(path, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(30, height - 50, "🧾 GPT-PayAudit - Audit Report")

    c.setFont("Helvetica", 12)
    c.drawString(30, height - 80, f"File: {filename}")
    c.drawString(30, height - 100, "Audit Summary:")
    
    text = c.beginText(30, height - 120)
    text.setFont("Helvetica", 10)
    for line in summary.split("\n"):
        text.textLine(line)
    c.drawText(text)

    y = height - 220
    c.drawString(30, y, "Flagged Transactions:")
    for txn in anomalies[:10]:  # show first 10
        y -= 20
        c.drawString(40, y, f"{txn}")

    c.save()
    return path
