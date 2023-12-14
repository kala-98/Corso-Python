import streamlit as st
import sys
import os

# dico a python di considerare anche la cartella padre per recuperare eventuali moduli
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import functions

todos = functions.get_todo()

# "allarga" la finestra
st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"] #session_state restituisce una sorta di dizionario
    todos.append(todo + "\n")
    functions.write_todo(todos)

st.title("Todo App")
st.subheader("My todo app")
st.write("This app is to increase your <b>productivity</b>",
         unsafe_allow_html=True)

# recupero la lista
for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[item]
        st.rerun()

st.text_input(label="Add new todo", placeholder="Enter new todo", 
              on_change=add_todo, key="new_todo")


#st.session_state
