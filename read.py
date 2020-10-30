import email
from imapclient import IMAPClient


from_mail = "your email is"
from_passw = 'your password'

try:
    conn = IMAPClient('imap.gmail.com', ssl=True)
    print("1 => ", conn)
except:
    print('Error occured while estalishing connection to imap server')

try:
    login = conn.login(from_mail, from_passw)
    print("2 => ", login)
except:
    print('Error occured while Login to gmail account')



select_folder = conn.select_folder("INBOX", readonly=True)
print("3 => ", select_folder)

messages = conn.search('UNSEEN')

for uid, message_data in conn.fetch(messages, 'RFC822').items():
    email_message = email.message_from_bytes(message_data[b'RFC822'])
    print(uid, email_message.get('From'), email_message.get('Subject'))


conn.logout()