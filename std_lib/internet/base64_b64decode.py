#! /usr/bin/env python3 

import base64

encoded_data = b'VGhpcyBpcyB0aGUgZGF0YSwgaW4gdGhlIGNsZWFyLg=='
decoded_data = base64.b64decode(encoded_data)

print(f'Encoded -> {encoded_data}')
print(f'Decoded -> {decoded_data}')