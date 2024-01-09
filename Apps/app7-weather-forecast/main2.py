import streamlit as st
import pandas as pd
import plotly.express as px
import random

st.title("In search for Happiness")

df = pd.read_csv("happy.csv", sep = ",")

# recupero le colonne
list_columns = list(df.columns)

if 'indexs' not in st.session_state:
    st.session_state['indexs'] = random.sample(range(len(list_columns)), 3)

options_x = [list_columns[id].replace("_", " ") for id in st.session_state['indexs']]
options_y = [list_columns[id].replace("_", " ") for id in st.session_state['indexs']]


# creazione delle selectbox
valueX = st.selectbox("Select the data for the X-axis", [""] + options_x, key="X")
valueY = st.selectbox("Select the data for the Y-axis", [""] + options_y, key="Y")


if valueX and valueY:
    st.header(f"{valueX} and {valueY}")

    columnX = valueX.replace(" ", "_")
    columnY = valueY.replace(" ", "_")

    # Creazione del grafico
    fig = px.scatter(df, x=df[columnX], y=df[columnY], labels={"x": valueX, "y": valueY})
    st.plotly_chart(fig)

st.write(st.session_state)
