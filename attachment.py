import smtplib

import email
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

from_email = "your email"
from_passw = "your passw"

# List of people you want to send to
to_email = ['', '']

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    print("1 => ", server)

    ehlo = server.ehlo()
    print('2 = >', ehlo)

    tsl = server.starttls()
    print('3 => ', tsl)
    print("Connection established successfully")
except Exception as e:
    print(e)


try:
    login = server.login(from_email, from_passw)
    print("Login successful")
except Exception as e:
    print(e)

message = MIMEMultipart()
message['Subject'] = 'write subject here'
message['From'] = 'from here'
message['To'] = ", ".join(to_email)


# Write below the body of the emails
messageText = MIMEText('''
Dear Sir/Ma'am

    ...



    
    Regards.
''')
message.attach(messageText)

# attach an image file here
with open("example.jpg", 'rb') as fp:
    image = MIMEImage(fp.read())
    image.add_header('Photo', 'Photo', filename='example.jpg')
message.attach(image)


# attach an pdf or ppt file here
pdf = MIMEApplication(open('example.pdf', 'rb').read())
pdf.add_header('Resume', 'attachment', filename='example.pdf')
message.attach(pdf)


try:
    server.send_message(message)
    server.quit()
    print("Email successfully sent")
except Exception as e:
    print("Error while sending email", e)