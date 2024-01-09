import streamlit as st 
import plotly.express as px

# front-end's creation
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecasted Days: ", min_value = 1, max_value = 5,
                 help = "Select the number of forecasted days") # with help they can see more information about the widget
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

if place != "":
    st.subheader(f"{option} for the next {str(days) + " day in " if days == 1 else str(days) + " days in "} {place}")

# making dynamic plot 
# requires a "fig" (we create it through data visualization library such as plotly)
dates = ["2022-25-10", "2022-26-10", "2022-27-10", "2022-28-10", "2022-29-10",]
temperatures = [10, 12, 15, 16, 13]

fig = px.line(x = dates[0:days], y = temperatures[0:days], labels= {"x": "Date", "y": "Temperatures (°C)"})
st.plotly_chart(fig)