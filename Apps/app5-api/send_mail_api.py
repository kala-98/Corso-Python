import smtplib, ssl
import os

def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "jersew98@gmail.com"
    password = os.getenv("PASSWORD") # recuperiamo la password attraverso la variabile d'ambiente che sarà accessibile solo dal nostro pc. Questo per evitare la proliferazione di informazioni sensibili
    receiver = "jersew98@gmail.com"

    context = ssl.create_default_context()

#     # implementazione della corretta formattazione per la visualizzazione della posta in Gmail
#     message_mail = f"""\
# Subject: new email from {user_email}

# From: {user_email} 
# Topic: {topic}
# {message}
# """

    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)