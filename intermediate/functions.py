import csv
FILEPATH = 'C:/Users/ervin/OneDrive/Desktop/Progetti/Corso Python/intermediate/data.csv'

def get_dataCsv(delimiter_arg, filepath = FILEPATH):
    lista = []
    with open(filepath, "r") as file:
        fileCsv = csv.reader(file, delimiter = delimiter_arg)
        for row in fileCsv:
            lista.append(row)

    return lista


if __name__ == "__main__":
    print("Hello")