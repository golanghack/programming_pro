#! /usr/bin/env python3 

"""Operation input/output."""

import requests 

response = requests.get('https://www.google.com') # input/output

items = response.headers.items()

# response study
headers = [f'{key} _. {header}' for key, header in items]

# concationation -> procssor bound
formatted_headers = '\n'.join(headers)

# input/otput
with open('headers.txt', 'w') as file:
    file.write(formatted_headers)
      
 