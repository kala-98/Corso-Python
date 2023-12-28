import pandas as pd
import glob 

# recupero tutti i file che corrispondono al pattern che ho definito
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name = "Sheet 1")
    print(df)
