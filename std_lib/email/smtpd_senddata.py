#! /usr/bin/env python3 

import smtplib
import email.utils
from email.mime.text import MIMEText

message = MIMEText('This is a message')
message['To'] = email.utils.formataddr(('Recipient', 'recipient@example.com'))
message['From'] = email.utils.formataddr(('Author', 'author@example.com'))
message['Subject'] = 'Simple subject'

server = smtplib.SMTP('localhost', 1025)
server.set_debuglevel(True)

try:
    server.sendmail('author@example.com', ['recipient@example.com'], message.as_string())
finally:
    server.quit()