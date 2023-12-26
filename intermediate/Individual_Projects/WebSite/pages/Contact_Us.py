import streamlit as st
from send_email import send_mail

#st.set_page_config(layout="wide")

with open("style.css", "r") as file:
    content_css = file.read()

custom_css = f"""
    <style>
    {content_css}
    </style>
"""

st.markdown(custom_css, unsafe_allow_html = True)

st.header("Contact Me")

# creazione del form per l'invio della mail (ottimizzato per account gmail)
with st.form(key = "email_form"):
    user_email = st.text_input("Your Email address")
    message = st.text_area("Your Message")
    button = st.form_submit_button("Submit")
    if button:
        send_mail(message, user_email)
        st.info("Your email has been sent successfully")