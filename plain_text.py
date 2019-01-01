#Python can also be used to send a plain text email
import smtplib, ssl
import getpass
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "me@gmail.com"
receiver_email = "me+person1@gmail.com"
#getting the password by getpass module, this will not show the password while entering
password = getpass.getpass("Type your password and press enter:",stream=None)
message = """\
Subject: Hi there!
Tried sending emails using python . """

context = ssl.create_default_context()
try:
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 
