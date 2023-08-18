#! /usr/bin/env python3 

from urllib import request

response = request.urlopen('https://example.com')
print('Response -> ', response)
print('URL -> ', response.geturl())

headers = response.info()
print('DATE -> ', headers['date'])
print('HEADERS')
print('--------')
print(headers)

data = response.read().decode('utf-8')
print('LENGHT -> ', len(data))
print('DATA')
print('----------')
print(data)