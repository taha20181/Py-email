import smtplib
import ssl
import email

from_email = ""
from_passw = ""

# uncomment below code to send cutomised emails in bulk
# create a list of dictionary contain name and email to send in bulk

# to_email = [{'name': '', 'email': ''}, {'name': '', 'email':''}, {'name':'', 'email':''}]


# uncomment below code to send common email in bulk
# enter email ids to send mail in the below list

to_email = ["", ""]


try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    print("1 => ", server)

    ehlo = server.ehlo()
    print("2 => ", ehlo)

    starttls = server.starttls()
    print("3 => ", starttls)
    print("Connection established successfully")
except:
    print("Error occured while setting up the connection to SMTP server")

try:
    login = server.login(from_email, from_passw)
    print("4 => ", login)

    print("Login successful")
except:
    print("Login Failed")


# uncomment below piece of code to send common email in bulk
try:
    email_content = email.message.Message()
    email_content['Subject'] = "enter subject here"
    email_content['From'] = "Your name "
    email_content['To'] = ", ".join(to_email)
    email_content['Body'] = '''
        Email body goes here
    '''
    server.send_message(email_content)
    print('Email sent successfully')
    server.quit()
except:
    print("Error occured while sending mail")




# uncomment below piece of code to send cutomized emails

# try:
#     for emails in to_email:
#         email_content = email.message.Message()
#         email_content['Subject'] = "enter subject here"
#         email_content['From'] = "Your name "
#         email_content['To'] = emails['email']
#         print('Sending to => ', emails['email'])
#         mail_body = """
#         Dear %s,
#             Body goes here
#         \n\n\n\n\n\n
        
#         This is a self generated message. Please Do not reply.""" % (emails['name'])

#         email_content.set_payload(mail_body)
#         server.send_message(email_content)
#     print('Email sent successfully')
#     server.quit()
# except:
#     print("Error occured while sending mail")