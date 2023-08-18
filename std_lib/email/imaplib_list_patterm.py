#! /usr/bin/env python3 

from imaplib_connect import open_connecttion

with open_connecttion() as conn:
    typ, data = conn.list(pattern='*Example*')

print('Response code -> ', typ)

for line in data:
    print('Server response -> ', line)
    