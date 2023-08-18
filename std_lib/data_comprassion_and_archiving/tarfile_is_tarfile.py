#! /usr/bin/env python3 

import tarfile

lst_files = ['READMY.txt', 'example.tar', 'bad_example.tar', 'nothere.tar']

for filename in lst_files:
    try:
        print(f'{filename:>15} {tarfile.is_tarfile(filename)}')
    except IOError as err:
        print(f'{filename:>15} {err}')