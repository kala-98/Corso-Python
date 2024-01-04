import os
import pandas as pd
import numpy as np

PATH = "data_small/"
def read_file_csv(station, date, filepath = PATH):

    lista = os.listdir(PATH)
    #lista_file = [file for file in lista if file.startswith("TG_")]
    fileName = [file for file in lista if file.endswith(f"{str(station)}.txt")]

    for file_tg in fileName:
        with open(PATH + file_tg, "r") as file:
            df = pd.read_csv(file, skiprows=20, parse_dates = ["    DATE"])

            # il metodo mask esclude tutti quelli con valore -9999 nella colonna "    TG" e gli sostituisce con nan
            df["TG0"] =  df["   TG"].mask(df["   TG"] == -9999, np.nan)
            # normalizzo i dati
            df["TG"] = df["TG0"] / 10

            result = df.loc[df["    DATE"] == date]["TG"]
            if result.dropna().empty:
                result = None  
                return "There are no information available for that date, sorry"
            else:
                result = result.squeeze()
                return result
            
if __name__ == "__main__":
    print("Ok")

                
            