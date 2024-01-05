# with open("dictionary.csv", "r") as file:
#     content = file.readlines()

import pandas as pd

df = pd.read_csv("dictionary.csv")
print(df)

# import os

# print(os.getcwd())