#! /usr/bin/env python3 

import base64

with open(__file__, 'r', encoding='utf-8') as file_input:
    raw = file_input.read()
    initial_data = raw.split('# end_header')[1]

byte_string = initial_data.encode('utf-8')
encoded_data = base64.b64encode(byte_string)

num_initial = len(byte_string)
# never will more 2 
padding = 3 - (num_initial % 3)

print(f'bytes before encoding -> {num_initial}')
print(f'Expect {padding} padding bytes')
print(f'{len(encoded_data)} bytes after encoding\n')
print(encoded_data)