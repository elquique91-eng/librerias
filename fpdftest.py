
from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=16)
pdf.cell(50,20, txt="helloo hi how are you")
pdf.output("C:/Users/elqui/OneDrive/Documentos/greet.pdf")
