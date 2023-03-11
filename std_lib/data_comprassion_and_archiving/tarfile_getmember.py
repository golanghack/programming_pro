#! usr/bin/env python3 

import tarfile
import time 

lst_files = ['READMY.txt', 'notthere.txt']

with tarfile.open('example.tar', 'r') as file:
    for filename in lst_files:
        try:
            info = file.getmember(filename)
        except KeyError:
            print(f'ERROR -> Did not find {filename} in tar archive')
            
        else:
            print(f'{info.name} is {info.size} bytes')