#email with HTML content and embed with images and attachments as PDFs
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

sender_email = "me@gmail.com"
receiver_email = "me+person1@gmail.com"
password = getpass.getpass("Type your password and press enter:",stream=None)

message = MIMEMultipart("alternative")
message["Subject"] = " Add the Subject here"
message["From"] = sender_email
message["To"] = receiver_email
#<img src="⁨HNY.jpg" alt="2019" width="500" height="333" align="middle">
# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
    <p><b>Hi,<br>
       Wishing you a very Happy New Year:D<br>
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message

#Attaching image embed in the email as well as an attachment

fp = open('HNY.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
message.attach(msgImage)

msgText = MIMEText('<b><i>"New Year<br><br>
New Moments<br><br>
New Adventures<br><br>
New Lessons<br><br>
New Memories<br><br>
New Challenges<br><br>
New Opportunities..."</b></i>
<br><br><body style="background-color:#4C9900;"></body>
<img src="https://img.timesnownews.com/story/1546096823-fina.jpg?d=600x450" align="middle">
<br><br><br>
.....<b><i>End each year with a few good lessons, start a new one by showing that you have learned lessons of past well<br><br>
A very HAPPY NEW YEAR in advance:)<br></b></i><br><br>Regards<br>XYZ<br>sent using Python', 'html')



message.attach(msgText)
# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string())
