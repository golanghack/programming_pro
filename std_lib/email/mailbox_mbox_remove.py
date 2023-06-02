#! /usr/bin/env python3 

import mailbox 

mbox = mailbox.mbox('example.mbox')
mbox.lock()

try:
    to_remove = []
    for key, value in mbox.iteritems():
        if '2' in value['subject']:
            print(f'Removing -> {key}')
            to_remove.append(key)
    for key in to_remove:
        mbox.remove(key)
finally:
    mbox.flush()
    mbox.close()

print(open('example.mbox', 'r', encoding='utf8').read())