# 1st scraping data's project
import requests
import selectorlib
import smtplib, ssl

URL = "http://programmer100.pythonanywhere.com/tours/"

# through this header we can emulate the browser's behaviour
HEADERS = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
          }
def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers = HEADERS)
    source = response.text
    return source 

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml") # define the yaml file for the output
    value = extractor.extract(source)["tours"] # retrieving the tag with the id defined inside "tours" (this one can be called whatever we want)
    return value

# def send_email(message):
#     host = "smtp.gmail.com"
#     port = 465

#     username = "jersew98@gmail.com"
#     # password = ''
#     receiver = "jersew98@gmail.com"
#     context = ssl.create_default_context()

#     with smtplib.SMTP_SSL(host, port, context = context) as server:
#         server.login(username, password)
#         server.send(username, receiver, message)

def store(extracted):
    with open("data.txt", "a") as file: # we use "a" in order to append and not overwrite the file
        file.write(extracted + "\n")

def read(extracted):
    with open("data.txt", "r") as file:
        return file.read()

if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)  
    content = read(extracted)
    if extracted != "No upcoming tours":
        if extracted not in content:
            store(extracted)
            #send_email()