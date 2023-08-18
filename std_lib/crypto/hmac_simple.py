#! /usr/bin/env python3 

import hmac
import hashlib

encoded_str = 'aaaaaaa'.encode()
digest_maker = hmac.new(b'secret-shared-key-goes-here', encoded_str, hashlib.sha256)

with open('lorem.txt', 'rb') as file:
    while True:
        block = file.read(1024)
        if not block:
            break
        digest_maker.update(block)

digest = digest_maker.hexdigest()
print(digest)