#! /usr/bin/env python3 

import hmac 
import hashlib

digest_maker = hmac.new(
    b'secret', 
    b'', 
    hashlib.sha256,
)

with open('hmac_sha.py', 'rb') as file:
    while True:
        block = file.read(1024)
        if not block:
            break
        digest_maker.update(block)

digest = digest_maker.hexdigest()
print(digest)