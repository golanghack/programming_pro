#! /usr/bin/env python3 

import imaplib
import imaplib_connect

imaplib.Debug = 4
with imaplib_connect.open_connecttion() as conn:
    conn.select('INBOX', readonly=True)
    typ, msg_data = conn.fetch('1', '(BODY.PEEK[HEADER] FLAGS)')
    print(msg_data)