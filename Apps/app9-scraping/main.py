# 1st scraping data's project
import requests
import selectorlib

URL = "http://programmer100.pythonanywhere.com/tours/"

# through this header we can emulate the browser's behaviour
HEADERS = {
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
          }
def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers = HEADERS)
    source = response.text
    return source 

if __name__ == "__main__":
    print(scrape(URL))