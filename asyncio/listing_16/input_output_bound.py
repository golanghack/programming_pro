#! /usr/bin/env python3 

import requests

response = requests.get('https://www.example.com', timeout=10)
items = response.headers.items()
headers = [f'{key} -> {header}' for key, header in items]
formatted = '\n'.join(headers)
with open('headers.txt', 'w', encoding='utf8') as output_file:
    output_file.write(formatted)