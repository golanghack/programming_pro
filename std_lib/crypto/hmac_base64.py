#! /usr/bin/env python3 

import base64
import hmac
import hashlib

with open('lorem.txt', 'rb') as file:
    body = file.read()

hash_file = hmac.new(
    b'secret', 
    body, 
    hashlib.sha1,
)

digest = hash_file.digest()
print(base64.encodestring(digest))