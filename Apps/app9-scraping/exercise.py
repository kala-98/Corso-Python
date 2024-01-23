import selectorlib
import requests 
import streamlit as st
import plotly.express as px
import datetime
import time



def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract2.yaml")
    value = extractor.extract(source)["home"]
    return value

URL = "https://programmer100.pythonanywhere.com/"

list_temperatures = []
list_dates = []

# while True:

now = datetime.datetime.now()
formattedTime = now.strftime("%m-%d-%Y %H:%M:%S")

response = requests.get(URL)
content = response.text

valore = extract(content)

with open("output/output_exercise.txt", "a") as file:
    file.write(f"{formattedTime}, {valore} \n")

with open("output/output_exercise.txt", "r") as file:
    content2 = file.readlines()

for element in content2:
    date = element.split(",")[0]
    temperature = element.split(",")[1]
    temperature = temperature.strip("\n")

    list_dates.append(date)
    list_temperatures.append(temperature)
    
st.header("Testing the scraping")
fig = px.line(x = list_dates, y = list_temperatures, labels = {"x": "Dates", "y": "temperatures"})
st.plotly_chart(fig)

# time.sleep(10)
