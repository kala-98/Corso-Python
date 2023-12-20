import streamlit as st 

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .appview-container {
    background-color:#808080;
    }
    img {
    width: 600px;
    height: 500px;
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
    st.info(content)

content2 = "Below you can find some apps i have built in Python. Feel free to contact me!"
st.write(content2)