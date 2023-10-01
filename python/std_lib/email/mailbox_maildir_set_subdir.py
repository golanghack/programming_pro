#! /usr/bin/env python3 

import mailbox
import os 

print('Before -> ')
mbox = mailbox.Maildir('Example')
mbox.lock()

try:
    for message_id, message in mbox.iteritems():
        print(f'{message.get_subdir():6} "{message["Subject"]}"')
        message.set_subdir('cur')
        mbox[message_id] = message
finally:
    mbox.flush()
    mbox.close()

print('\nAfter -> ')
mbox = mailbox.Maildir('Example')
for message in mbox:
    print(f'{message.get_subdir():6} "{message["Subject"]}"')

print()
for dirname, subdirs, files in os.walk('Example'):
    print(dirname)
    print('Directories -> ', subdirs)
    for name in files:
        fullname = os.path.join(dirname, name)
        print(fullname)