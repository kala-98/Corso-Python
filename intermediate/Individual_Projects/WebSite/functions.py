# import pandas as pd 

# def get_csv(pathCsv, sep = ','):
#     """Definizione di una funzione per leggere i valori da un file csv
#        parametrizzando il numero delle righe che mi interessa acquisire,
#        il tutto attraverso la libreria pandas
#     """
#     df = pd.read_csv(pathCsv, sep)


# if __name__ == "__main__":
#     print("Hello")

with open("style.css", "r") as file:
    content = file.read()

print(content)