#! /usr/bin/env python3 

import imaplib
import imaplib_connect
from imaplib_list_parse import parse_list_response

with imaplib_connect.open_connecttion() as conn:
    typ, mbox_data = conn.list()
    for line in mbox_data:
        flags, delimiter, mbox_name = parse_list_response(line)
        conn.select(f"'{mbox_name}'", readonly=True)
        typ, msg_ids = conn.search(None, 'ALL')
        print(mbox_name, typ, msg_ids)