import requests
import streamlit as st

def set_theme(theme):
    if theme == "Light Mode":
        st.markdown(
            """
            <style>
            .appview-container {
            background-color: white;
            }
            p {
            color: black;
            }
            .st-emotion-cache-10trblm {
            color : black;
            }

            .st-emotion-cache-x78sv8 p  {
                color: white;
            }

            .st-at.st-au.st-av.st-aw.st-ae.st-ag.st-ah.st-af.st-bz.st-bo.st-ai.st-aj.st-ak.st-al.st-am.st-an.st-ao.st-ap.st-c0.st-ar.st-as.st-bb.st-b3.st-b4.st-b5.st-b6.st-b7:hover {
            cursor: pointer;
        }

            </style>
            """,
            unsafe_allow_html=True
        )
    elif theme == "Dark Mode":
        st.markdown(
            """
            <style>
            .appview-container {
            background-color: black;
            }
            p {
            color: white;
            }
            .st-emotion-cache-10trblm {
            color : whitek
            }

            .st-emotion-cache-x78sv8 p  {
                color: black;
            }

            .st-at.st-au.st-av.st-aw.st-ae.st-ag.st-ah.st-af.st-bz.st-bo.st-ai.st-aj.st-ak.st-al.st-am.st-an.st-ao.st-ap.st-c0.st-ar.st-as.st-bb.st-b3.st-b4.st-b5.st-b6.st-b7:hover {
            cursor: pointer;
            }
          </style>
            """,
            unsafe_allow_html=True
        )

# scegli il tema tramite un widget
theme_choice = st.selectbox("Seleziona il tema", ["Light Mode", "Dark Mode"])
set_theme(theme_choice)

api_key = "cc9v9sT8CMSPjHJM8ql9AGEmQU1Na7kVt9knzPYL"

response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")
image_filepath = "img.png"

if response.status_code == 200:
    content = response.json()
    print(content)
    if 'url' in content:
        title = content["title"]
        image_url = content["url"]
        description = content["explanation"]

        response2 = requests.get(image_url)

        with open(image_filepath, "wb") as file:
            file.write(response2.content) # questo content è diverso da quello definito sopra

        st.header(title)
        st.image(image_url)
        st.write(description)
    else:
        st.warning("Nessuna immagine disponibile per la data specificata.")
else:
    st.error(f"Errore nella richiesta HTTP: {response.status_code}")

