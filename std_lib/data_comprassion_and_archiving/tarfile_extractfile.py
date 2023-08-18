#! /usr/bin/env python3 

import tarfile

lst_file = ['READMY.txt', 'notthere.txt']

with tarfile.open('example.tar', 'r') as file:
    for filename in lst_file:
        try:
            f = file.extractfile(filename)
        except KeyError:
            print(f'ERROR -> Did not find {filename} in tar archive')
        else:
            print(filename, ':')
            print(file.read().decode('utf-8'))