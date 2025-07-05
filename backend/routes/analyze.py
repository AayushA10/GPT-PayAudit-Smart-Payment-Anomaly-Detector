from fastapi import APIRouter
from backend.services.anomaly_detector import detect_anomalies
from backend.services.gpt_explainer import explain_anomalies
from backend.services.report_generator import generate_pdf_report

router = APIRouter(prefix="/analyze", tags=["Analysis"])

@router.get("/{filename}")
def analyze_file(filename: str):
    result = detect_anomalies(filename)
    explanation = explain_anomalies(result)

    # ⬇️ Generate PDF
    generate_pdf_report(filename, explanation, result)

    return {
        "raw": result,
        "gpt_summary": explanation,
        "report_path": f"data/{filename}_report.pdf"
    }
