import streamlit as st
import sys
import os

# dico a python di considerare anche la cartella padre per recuperare eventuali moduli
sys.path.append('..')
import functions

st.title("Todo App")
st.subheader("My todo app")
st.write("This app is to increase your productivity")

todos = functions.get_todo()
unique_value = 0

# recupero la lista
for item in todos:
    unique_value += 1
    st.checkbox(item, key=f"todo{unique_value}")

st.text_input(label="", placeholder="Enter new todo")
