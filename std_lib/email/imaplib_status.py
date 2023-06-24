#! /usr/bin/env python3 

import re 
import imaplib
from imaplib_list_parse import parse_list_response
from imaplib_connect import open_connecttion

with open_connecttion() as conn:
    typ, data = conn.list()
    for line in data:
        flags, delimiter, mailbox = parse_list_response()
        print('Mailbox -> ', mailbox)
        status = conn.status(
            f'"{mailbox}"',
            '(MESSAGE RECENT UIDNEXT UIDVALIDITY UNSEEN)',
        )
        print(status)