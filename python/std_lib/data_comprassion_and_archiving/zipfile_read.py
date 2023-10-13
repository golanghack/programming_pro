#! /usr/bin/env python3 

import zipfile

with zipfile.ZipFile('example.zip') as file:
    for filename in ['README.txt', 'notthere.txt']:
        try:
            data = file.read(filename)
        except KeyError:
            print(f'ERROR -> Did not find {filename} in zip file')
        else:
            print(filename, ':')
            print(data)
            print()
            
            