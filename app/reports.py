
from fastapi import APIRouter
from fpdf import FPDF

router = APIRouter()

@router.get("/pdf")
def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Vitulo Livestock Report", ln=True)
    file_path = "/tmp/report.pdf"
    pdf.output(file_path)
    return {"report_path": file_path}
