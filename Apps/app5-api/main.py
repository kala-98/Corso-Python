import requests

# # creation of a template for request
# url = "https://finance.yahoo.com"
# # making request 
# request = requests.get(url)
# # retrieving the content (receiving in this case the whole html/js code)
# content = request.text
# with open("api_news.json", "w", encoding="utf-8") as file:
#     file.write(content)



api_key = "9f1d25fb9da449bd88743c2f333f79b8"

# request to get news about Tesla (from newsapi.org)
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-11-29&sortBy=publishedAt&apiKey=9f1d25fb9da449bd88743c2f333f79b8"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])
  




