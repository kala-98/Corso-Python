import pandas as pd
import glob
from fpdf import FPDF
from datetime import date
from pathlib import Path

# recupero tutti i file che corrispondono al pattern che ho definito
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    lista = []
    total_price = 0
    df = pd.read_excel(filepath, sheet_name = "Sheet 1")
    
    # creazione del pdf per ogni file
    pdf = FPDF(orientation = "P", unit = "mm", format = "A4")
    pdf.set_auto_page_break(auto = False, margin = 0)
    pdf.add_page()
    pdf.add_font('Ubuntu', "", 'Ubuntu-R.ttf', uni=True)
    pdf.add_font('Ubuntu-Bold', "", 'Ubuntu-Bold.ttf', uni=True)
    pdf.set_font('Ubuntu', size = 14)
    pdf.set_text_color(0, 0, 0) #rgb

    # recupero solo il nome del file dal path
    nameFile = Path(filepath).stem 
    # recupero il numero della fattura
    invoiceNumber = nameFile.split("-")[0]
    # recupero la data odierna (nel formato che mi interessa)
    actualDate = date.today()
    formattedDate = actualDate.strftime("%d-%m-%Y")

    pdf.cell(w = 12, h = 12, txt = "Invoice nr: " + invoiceNumber, align = "L", ln = 1, border = 0)
    pdf.cell(w = 12, h = 12, txt = "Date: " + formattedDate, align = "L", ln = 1, border = 0)
    pdf.ln(4)

    # header 
    pdf.set_font('Ubuntu-Bold', size = 14)
    cols_header = df.columns.ravel()
    for col_header in cols_header:
        
        text_width = pdf.get_string_width(col_header)
        col_header = col_header.title().replace("_", " ")
        
        if col_header == "Product Name":
            border_width = text_width + 40
        elif col_header == "Amount Purchased":
            col_header = "Amount"
            text_width = pdf.get_string_width(col_header)
            border_width = text_width + 5           
        else:
            border_width = text_width + 5
        lista.append(border_width)
        pdf.cell(w = border_width, h = 12, txt = col_header, align = "C", ln = 0, border = 1)       
  
    pdf.ln(12)
    
    # data
    pdf.set_font('Ubuntu', size = 14)
    for index, row in df.iterrows():
        for index, col_name in enumerate(df.columns):

            lunghezza_colonna = pdf.get_string_width(str(row[col_name]))

            # gestione nel caso la lunghezza del testo sia minore del doppio del testo
            if lunghezza_colonna > lista[index] and lunghezza_colonna <= lista[index] * 2:

                pdf.multi_cell(w = lista[index], h = 6, txt = str(row[col_name]), align = "L", border = 1)
                pdf.set_y(pdf.get_y() - 12)
                nuova_coordinata_x = pdf.get_x() + 104.39 
                pdf.set_x(nuova_coordinata_x)

            # lunghezza minore al triplo del testo
            elif lunghezza_colonna > lista[index] and lunghezza_colonna <= lista[index] * 3:

                pdf.set_font('Ubuntu', size = 12)
                pdf.multi_cell(w = lista[index], h = 4, txt = str(row[col_name]), align = "L", border = 1)
                pdf.set_y(pdf.get_y() - 12)
                nuova_coordinata_x = pdf.get_x() + 104.39 
                pdf.set_x(nuova_coordinata_x)

            elif lista[index] != lista[-1]:

                pdf.set_font('Ubuntu', size = 14)
                pdf.cell(w = lista[index], h=12, txt=str(row[col_name]), align="L", ln=0, border=1)
            else:

                pdf.set_font('Ubuntu', size = 14)
                pdf.cell(w = lista[index], h=12, txt=str(row[col_name]), align="L", ln=1, border=1)

        # pdf.cell(w = lista[0], h = 12, txt = str(row["product_id"]), align = "L", ln = 0, border = 1)
        # pdf.cell(w = lista[1], h = 12, txt = str(row["product_name"]), align = "L", ln = 0, border = 1)
        # pdf.cell(w = lista[2], h = 12, txt = str(row["amount_purchased"]), align = "L", ln = 0, border = 1)
        # pdf.cell(w = lista[3], h = 12, txt = str(row["price_per_unit"]), align = "L", ln = 0, border = 1)
        # pdf.cell(w = lista[4], h = 12, txt = str(row["total_price"]), align = "L", ln = 1, border = 1)
        total_price += row["total_price"]
   
    # creation row for total price
    for i in range(len(lista) - 1):
        pdf.cell(w = lista[i], h = 12, txt = "", align = "L", ln = 0, border = 1)
        
    pdf.cell(w = lista[-1], h = 12, txt = str(total_price), align = "L", ln = 1, border = 1)

    pdf.ln(12)

    pdf.cell(w = 12, h = 12, txt = "The total amount is: " + str(total_price) + "€", align = "L", ln = 1, border = 0)

    #pdf.ln(30)

    pdf.image("images/logo.png", x = 120, w = 65, h = 80)

    pdf.output("Invoice_" + nameFile + '.pdf')