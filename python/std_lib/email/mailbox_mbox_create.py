#! /usr/bin/env python3 

import mailbox
import email.utils

from_addr = email.utils.formataddr(('Author', 'author@author.com'))
to_addr = email.utils.formataddr(('Recipient', 'recipient@recipient.com'))

payload = 'This is a body text. There are one line'

mbox = mailbox.mbox('example.mbox')
mbox.lock()

try:
    message = mailbox.mboxMessage()
    message.set_unixfrom('author -> Feb 4 02:05:44 2023')
    message['From'] = from_addr
    message['To'] = to_addr
    message['Subject'] = 'Sample message 1'
    message.set_payload(payload)
    mbox.add(message)
    mbox.flush()

    message = mailbox.mboxMessage()
    message.set_unixfrom('author')
    message['From'] = from_addr
    message['To'] = to_addr
    message['Subject'] = 'Sample message 2'
    message.set_payload('This is second body.\n')
    mbox.add(message)
    mbox.flush()
finally:
    mbox.unlock()

print(open('example.mbox', 'r', encoding='utf8').read())
