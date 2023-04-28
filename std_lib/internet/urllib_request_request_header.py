#! /usr/bin/env python3 

from urllib import request  

req = request.Request('https://nasa.gov')
req.add_header('User_agent', '')

response = request.urlopen(req)
data = response.read().decode('utf-8')

print(data)