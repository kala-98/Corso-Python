#importing the class "Flask" which create website object instances
from flask import Flask, render_template
import pandas as pd
import os
import functions as fn
from datetime import datetime

# it's possibile to define other static paths with static_url_path, beyond the default one "static"
app = Flask(__name__, static_url_path='/static')

# applying route method to the object app
# make sure to add the html pages inside the "templates" folder 
# the images and css has to be in a folder called "static"
# and render them through the render_template function
path = "data_small/"

# retrieving the information from stations which will be formatted into html table
stations = pd.read_csv(path + "stations.txt", skiprows = 17)
# defining the columns i want to retrieve
stations = stations[["STAID","STANAME                                 "]]
stations.columns = ['Station ID', 'Station Name']
stations_html = stations.to_html(classes='table-class', index=False)

@app.route("/")
def home():
    return render_template("home.html", data = stations_html)

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # leggo i valori dal file
    temperature = fn.read_file_csv(station, date)
    # converto la stringa date in un oggetto datetime e poi applico il formato che mi interessa
    date_formatted = datetime.strptime(date, "%Y%m%d").strftime("%d-%m-%Y")
    return {"station": station,
            "date": date_formatted,
            "temperature": temperature}

@app.route("/api/v1/<station>")

# my solution
# def about_station(station):
#      result = ""
#      # recupero le temperature di tutti i giorni analizzati relativi a quella stazione
#      temperatureStazione = fn.read_file_csv(station) # lista
#      for element in temperatureStazione:
#          result += '{"station": ' + str(station) + ', "date":' + str(element[0][0:10]) + ', "temperature": ' + str(element[1]) + '} <br> <br>'
                         
#      return result

# teacher's solution
def about_station(station):
     fileName = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
     df = pd.read_csv(fileName, skiprows = 20, parse_dates = ["    DATE"])
     result = df.to_dict(orient = "records")     
     return result

@app.route("/api/v1/yearly/<station>/<year>")
def about_station_date(station, year):
     fileName = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
     df = pd.read_csv(fileName, skiprows = 20)

     # convert the number column into a string
     df["    DATE"] = df["    DATE"].astype(str)
     result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient = "records")
     return result

# the app has to enabled only when we run this script directly
# in order to run multiple apps, we can specify the port number
if __name__ == "__main__":
   app.run(debug = True, port = 5001)

