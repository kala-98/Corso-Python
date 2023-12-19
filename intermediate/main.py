import csv
with open("intermediate/data.csv", "r") as file:
    contenuto = csv.reader(file, delimiter = ";")
    for row in contenuto:
        print(row)
    
        