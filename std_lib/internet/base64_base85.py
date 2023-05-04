#! /usr/bin/env python3 


import base64

original_data = b'This is data'
print(f'Original data -> {len(original_data)} bytes {original_data!r}')

b64_data = base64.b64encode(original_data)
print(f'b64 Encoding -> {len(b64_data)} bytes {b64_data!r}')

b85_data = base64.b85encode(original_data)
print(f'b85 Encoded -> {len(b85_data)} bytes {b85_data!r}')

a85_data = base64.a85encode(original_data)
print(f'a85 Encode -> {len(a85_data)} bytes {a85_data!r}')