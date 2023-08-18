#! /usr/bin/env python3 

import zipfile

with zipfile.ZipFile('example.zip') as z_file:
    for filename in ['README.txt', 'notthere.txt']:
        try:
            info = z_file.getinfo(filename)
        except KeyError:
            print(f'ERROR -> did not find {filename} in zip file')
        else:
            print(f'{info.filename} is {info.file_size} bytes')
            
            