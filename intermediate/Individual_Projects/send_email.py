import smtplib, ssl # mail library that creates session

host = "smtp.gmail.com"
port = 465

username = "jersew98@gmail.com"
password = "test"

receiver = "jersew98@gmail.com"

context = ssl.create_default_context()
message = "Ciao come stai"

with smtplib.SMTP_SSL(host, port, context = context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
