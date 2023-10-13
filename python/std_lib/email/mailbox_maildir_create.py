#! /usr/bin/env python3 

import mailbox
import email.utils
import os 

from_addr = email.utils.formataddr(('Author', 'author@author.com'))
to_addr = email.utils.formataddr(('Recipient', 'recipient@recipient.com'))

payload = 'This is message'

mbox = mailbox.Maildir('Example')
mbox.lock()

try:
    message = mailbox.mboxMessage()
    message.set_unixfrom('author Sat Jan 4 01:05:45 2023')
    message['From'] = from_addr
    message['To'] = to_addr
    message['Subject'] = 'Sample message 1'
    message.set_payload(payload)
    mbox.add(message)
    mbox.flush()

    message = mailbox.mboxMessage()
    message.set_unixfrom('author Sat Feb 4 02:04:04 2023')
    message['From'] = from_addr
    message['To'] = to_addr
    message['Subject'] = 'Sample message 2'
    message.set_payload('This is the second message body.\n')
    mbox.add(message)
    mbox.flush()
finally:
    mbox.unlock()


for dirname, subdirs, files in os.walk('Example'):
    print(dirname)
    print(f'Directories -> {subdirs}')
    for name in files:
        fullname = os.path.join(dirname, name)
        print('\n***', fullname)
        print(open(fullname, encoding='utf8').read())
        print('*' * 20)