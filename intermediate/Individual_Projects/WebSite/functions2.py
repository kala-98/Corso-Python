# import pandas as pd 

# def get_csv(pathCsv, sep = ','):
#     """Definizione di una funzione per leggere i valori da un file csv
#        parametrizzando il numero delle righe che mi interessa acquisire,
#        il tutto attraverso la libreria pandas
#     """
#     df = pd.read_csv(pathCsv, sep)

import csv
FILEPATH = 'C:/Users/ervin/OneDrive/Desktop/Progetti/Corso Python/intermediate/data.csv'

def get_dataCsv(delimiter_arg, filepath = FILEPATH):
    lista = []
    with open(filepath, "r") as file:
        fileCsv = csv.reader(file, delimiter = delimiter_arg)
        for row in fileCsv:
            lista.append(str(row))

    return lista


# if __name__ == "__main__":
#     print("Hello")

