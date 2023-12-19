import streamlit as st 

st.markdown(
    """
    <style>
    .appview-container {
    background-color:#808080;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ervin")
    content = """
    Hi i'm a young motivated guy, 
    eager to learn some skills about 
    coding in Python
    """
    st.write(content)