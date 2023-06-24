#! /usr/bin/env python3

import imaplib_connect

with imaplib_connect.open_connecttion() as conn:
    typ, data = conn.select('INBOX')
    print(typ, data)
    num_messages = int(data[0])
    print(f'The are {num_messages} messages in INBOX')