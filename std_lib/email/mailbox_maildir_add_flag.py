#! /usr/bin/env python3 

import mailbox 

print('Before -> ')
mbox = mailbox.Maildir('Example')
mbox.lock()

try:
    for message_id, message in mbox.iteritems():
        print(f'{message.get_flags():6} "{message["subject"]}"')
        message.add_flag('F')
        # update 
        mbox[message_id] = message
finally:
    mbox.flush()
    mbox.close()

print('\nAfter -> ')
mbox = mailbox.Maildir('Example')
for message in mbox:
    print(f'{message.get_flags():6} "{message["subject"]}"')
