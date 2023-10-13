#! /usr/bin/env 

from imaplib_connect import open_connecttion

with open_connecttion() as conn:
    typ, data = conn.list(directory='Example')

print('Respnonse code -> ', typ)

for line in data:
    print('Server response -> ', line)