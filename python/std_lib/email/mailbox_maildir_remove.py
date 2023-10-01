#! /usr/bin/env python3 

import mailbox
import os 

mbox = mailbox.Maildir('Example')
mbox.lock()

try:
    to_remove = []
    for key, message in mbox.iteritems():
        if '2' in message['subject']:
            print(f'Removing -> {key}')
            to_remove.append(key)
    for key in to_remove:
        mbox.remove(key)
finally:
    mbox.flush()
    mbox.close()

for dirname, subdirs, files in os.walk('Example'):
    print(dirname)
    print(f'Direcotries -> {subdirs}')
    for name in files:
        fullname = os.path.join(dirname, name)
        print('\n***', fullname)
        print(open(fullname, encoding='utf8').read())
        print('*' * 25)