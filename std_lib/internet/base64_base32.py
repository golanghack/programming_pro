#! /usr/bin/env python3 


import base64

original_data = b'This is the data'
print(f'Original data -> {original_data}')

encoded_data = base64.b32encode(original_data)
print(f'Encoding -> {encoded_data}')

decoded_data = base64.b32decode(encoded_data)
print(f'Decode -> {decoded_data}')