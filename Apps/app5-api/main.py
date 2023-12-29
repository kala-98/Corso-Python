import requests
import send_mail_api

# # creation of a template for request
# url = "https://finance.yahoo.com"
# # making request 
# request = requests.get(url)
# # retrieving the content (receiving in this case the whole html/js code)
# content = request.text
# with open("api_news.json", "w", encoding="utf-8") as file:
#     file.write(content)

topic = "microsoft"

api_key = "9f1d25fb9da449bd88743c2f333f79b8"

# request to get news about Tesla (from newsapi.org)
url = f"https://newsapi.org/v2/everything?q={topic}&from=2023-11-29&sortBy=publishedAt&apiKey=9f1d25fb9da449bd88743c2f333f79b8&language=en"

request = requests.get(url)
content = request.json()

body = f"""\
Subject: {topic.title()}'s Newsletter

"""

for article in content["articles"][:20]:  
    if article["title"] is not None and article["description"] is not None:
        body = body + article["title"] + "\n" + article["description"] \
        + "\n" + article["url"] + 2 * "\n"
body = body.encode("utf-8") 
send_mail_api.send_mail(message = body)
    # else:
    #     print("Skipping article with missing title or body.")
   
    
   
  




