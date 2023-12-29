from fpdf import FPDF
import glob 
from pathlib import Path

pdf = FPDF("P", "mm", "A4")

filePaths = glob.glob("exercise/Text+Files/*.txt")

for filePath in filePaths:
    pdf.add_page()
    pdf.set_auto_page_break(auto = False, margin = 0)
    pdf.add_font('Ubuntu', "", 'Ubuntu-R.ttf', uni=True)
    pdf.add_font('Ubuntu-Bold', "", 'Ubuntu-Bold.ttf', uni=True)
    pdf.set_text_color(0, 0, 0) 

    with open(filePath, "r") as file:
        content = file.read()

    fileName = Path(filePath).stem

    # title
    pdf.set_font('Ubuntu-Bold',  size = 18)
    pdf.cell(w = 0, h = 12, txt = fileName.title(), ln = 2, border = 0)

    # body
    pdf.set_font('Ubuntu',  size = 14)
    pdf.multi_cell(w = 0, h = 7, txt = content)

pdf.output("exercise.pdf")
    
