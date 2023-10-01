#! /usr/bin/env python3 

import smtplib
import email.utils
from email.mime.text import MIMEText
import getpass

to_email = input('Recipient -> ')
servername = input('Mail server name -> ')
serverport = input('Server port -> ')
if serverport:
    serverport = int(serverport)
else:
    serverport = 25

use_tls = input('User TLS (yes/no) -> ').lower()
username = input('Mail username -> ')
password = getpass.getpass("%s's password -> " % username)

# create message 
message = MIMEText('Test message')
message.set_unixfrom('author')
message['To'] = email.utils.formataddr(('Recipient', to_email))
message['From'] = email.utils.formataddr(('Author', 'author@example.com'))
message['Subject'] = 'Test'

if use_tls == 'yes':
    print('Starting with a secure connection')
    server = smtplib.SMTP_SSL(servername, serverport)
else:
    print('Starting with an insecure connection')
    server = smtplib.SMTP(servername, serverport)
try:
    server.set_debuglevel(True)

    # identification
    server.ehlo()

    # use TLS
    if server.has_extn('STARTING'):
        print('(starting TLS)')
        server.starttls()
        server.ehlo()
    else:
        print('(no STARTTLS)')
    
    if server.has_extn('AUTH'):
        print('(logging in)')
        server.login(username, password)
    else:
        print('(no AUTH)')
    server.sendmail('author@example.com', [to_email], message.as_string())
finally:
    server.quit()