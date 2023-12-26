import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

with open("style.css", "r") as file:
    content_css = file.read()

custom_css = f"""
    <style>
    {content_css}
    </style>
"""

st.markdown(custom_css, unsafe_allow_html = True)

st.title("The Best Company")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras iaculis mauris ut orci malesuada iaculis. Nam nisi nulla, sagittis sit amet erat ut, cursus iaculis neque. In vehicula felis sed molestie congue. Nulla aliquet enim eu tempus sodales. Quisque egestas, eros eget facilisis dignissim, felis nulla lacinia lectus, in rutrum augue enim vitae metus. Sed commodo facilisis suscipit. Ut a sem in orci aliquam porta at et ligula. Sed eu mauris ultrices, accumsan enim eget, lobortis mauris.")

st.subheader("Our team")

col1, col2, col3 = st.columns(3)

df = pd.read_csv("data.csv", sep = ",")

with col1:
    for index, row in df[:4].iterrows():
        nome = row["first name"] + ' ' + row["last name"]
        st.subheader(nome.title())        
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        nome = row["first name"] + ' ' + row["last name"]
        st.subheader(nome.title())
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:12].iterrows():
        nome = row["first name"] + ' ' + row["last name"]
        st.subheader(nome.title())
        st.write(row["role"])
        st.image("images/" + row["image"])
