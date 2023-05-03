import smtplib,ssl
import os
host="smtp.gmail.com"
port=465
def send_email(message):
    username="aiman.khan.personal.78605@gmail.com"
    password=os.getenv("PASSWORD")

    context=ssl.create_default_context()
    reciver="aiman.khan.personal.78605@gmail.com"

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,reciver,message)
