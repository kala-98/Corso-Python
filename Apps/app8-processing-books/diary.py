import streamlit as st
import plotly.express as px
import glob 
from nltk.sentiment import SentimentIntensityAnalyzer
from datetime import datetime

lista_filePath = glob.glob("diary/*.txt")

list_pos = []
list_neg = []

dates = [name.strip(".txt").strip("diary\\") for name in lista_filePath]

analyzer = SentimentIntensityAnalyzer()

for filePath in lista_filePath:
    with open(filePath, "r") as file:
        content = file.read()
        scores = analyzer.polarity_scores(content)
        list_pos.append(scores["pos"])
        list_neg.append(scores["neg"])

st.title("Diary Tone")
st.subheader("Positivity")

fig = px.line(x = dates, y = list_pos, labels = {"x": "Date", "y": "Positivity"})
st.plotly_chart(fig)

st.subheader("Negativity")
fig = px.line(x = dates, y = list_neg, labels = {"x": "Date", "y": "Negativity"})
st.plotly_chart(fig)

