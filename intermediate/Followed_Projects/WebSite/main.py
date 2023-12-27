import streamlit as st 
import functions as fn

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');
    html, body, [class*="css"]  {
    font-family: 'Ubuntu', sans-serif !important;
    }
    .appview-container {
    background-color:#808080;
    }
    img {
    width: 600px;
    height: 500px;
    }
    #info {
    font-size: 40px;
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

content2 = "<span id='info'> Below you can find some apps i have built in Python. Feel free to contact me! </span>"
st.write(content2, unsafe_allow_html = True)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5]) # definisco il ratio delle dimensioni delle colonne
content3 = fn.get_dataCsv(";")

with col3:
    
    for i in range(1, len(content3), 2):
        st.title(content3[i][0])
        st.subheader(content3[i][1])
        st.write(f"[Source Code]({content3[i][2]})") # estrarre un link
        st.image("images/" + content3[i][3], use_column_width="auto")

with col4:

    for i in range(2, len(content3), 2):
        st.title(content3[i][0])
        st.subheader(content3[i][1])
        st.write(f"[Source Code]({content3[i][2]})")
        st.image("images/" + content3[i][3], use_column_width="auto")
        