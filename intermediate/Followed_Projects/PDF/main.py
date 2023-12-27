from fpdf import FPDF
import pandas as pd

# # creiamo una istanza pdf attraverso la classe FPDF
# # orientation P sta per portrait (verticale) mentre L indica landscape (orizzontale)
# pdf = FPDF(orientation = "P", unit = "mm", format = "A4")

# # applichiamo un metodo all'oggetto pdf per avere la pagina
# pdf.add_page()

# pdf.set_font(family = "Times", style = "B", size = 12)

# # width - height (mantieni lo stesso del size del font) - text - align: left - line break (tenerlo a 1)
# pdf.cell(w = 0, h = 12, txt = "Hello There!", align = "L", ln = 1, border = 1)
# pdf.cell(w = 0, h = 12, txt = "Hi There!", align = "L", ln = 1, border = 1)

# pdf.output("output.pdf") # va a sovrascrivere il file se esiste già

pdf = FPDF(orientation = "P", unit = "mm", format = "A4")
pdf.set_auto_page_break(auto = False, margin = 0)

df = pd.read_csv("topics_pdf.csv", sep = ",")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.add_font('Ubuntu', "", 'Ubuntu-R.ttf', uni=True)
    pdf.set_font('Ubuntu', size = 24)
    pdf.set_text_color(0, 0, 254) #rgb
    topic = row["Topic"]

    # header
    # recupero la lunghezza della stringa per rendere il bordo dinamico
    text_width = pdf.get_string_width(topic)
    border_width = text_width + 5
    pdf.cell(w = border_width, h = 12, txt = topic, align = "C", ln = 1, border = 1)

    # x1 e y1 definiscono il punto d'inizio della linea, x2 e y2 la fine
    # a4's paper width is 210mm
    for y in range(32, 283, 10):
        pdf.line(x1 = 10, y1 = y, x2 = 200, y2 = y)

    # footer
    # a4's paper height is 298mm
    pdf.ln(260)
    pdf.set_font('Ubuntu', size = 8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w = 0, h = 10, txt = topic, align = "R") 

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        for y in range(20, 281, 10):
            pdf.line(x1 = 10, y1 = y, x2 = 200, y2 = y)

        # footer
        pdf.ln(272)
        pdf.set_font('Ubuntu', size = 8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w = 0, h = 10, txt = topic, align = "R") 

pdf.output("output.pdf")