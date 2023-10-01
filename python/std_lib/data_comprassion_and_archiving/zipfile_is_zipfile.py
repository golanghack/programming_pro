#! /usr/bin/env python3 

import zipfile

lst_files = ['READMY.txt', 'example.zip', 'bad_example.zip', 'notthere.zip']

for filename in lst_files:
    print(f'{filename:>15} {zipfile.is_zipfile(filename)}')