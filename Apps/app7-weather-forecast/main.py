import streamlit as st 
import plotly.express as px
from backend import get_data
try:
    # front-end's creation
    st.title("Weather Forecast for the Next Days")
    place = st.text_input("Place: ")

    days = st.slider("Forecasted Days: ", min_value = 1, max_value = 5,
                    help = "Select the number of forecasted days") # with help they can see more information about the widget
    option = st.selectbox("Select data to view", ("Temperature", "Sky"))

    if place:


        # get the temperature/sky data
        filtered_data = get_data(place, days)

        # making dynamic plot 
        #requires a "fig" (we create it through data visualization library such as plotly)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            fig = px.line(x = dates, y = temperatures, labels= {"x": "Date", "y": "Temperatures (°C)"})
            st.subheader(f"{option} for the next {str(days) + " day in " if days == 1 else str(days) + " days in "} {place}")
            st.plotly_chart(fig)

        if option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain":"images/rain.png", "Snow":"images/snow.png"}
            image_path = [images[condition] for condition in sky_conditions]
            st.subheader(f"{option} for the next {str(days) + " day in " if days == 1 else str(days) + " days in "} {place}")
            st.image(image_path, width = 115)

except KeyError:
    st.write('<span style="color:red; font-size:30px">Please insert a valid city </span>', unsafe_allow_html=True)

