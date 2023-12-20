import streamlit as st 
import functions as fn

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

col3, col4 = st.columns(2)
content3 = fn.get_dataCsv(";")

with col3:
    
    for i in range(1, len(content3), 2):
        st.title(content3[i][0])
        st.subheader(content3[i][1])
        st.image("images/" + content3[i][3], use_column_width="auto")

with col4:

    for i in range(2, len(content3), 2):
        st.title(content3[i][0])
        st.subheader(content3[i][1])
        st.image("images/" + content3[i][3], use_column_width="auto")