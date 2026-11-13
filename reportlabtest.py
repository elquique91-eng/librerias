from reportlab.pdfgen import canvas
pdf=canvas.Canvas("archivo.pdf")
pdf.drawString(100, 750, "hola a todos gente!!!")
pdf.save()