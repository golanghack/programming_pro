#! /usr/bin/env python3 

import tarfile

print('___CREATING ARCHIVE___')
with tarfile.open('tarfile_append.tar', mode='w') as file:
    file.add('README.txt')
    
print('contents -> ')
with tarfile.open('tarfile_append.tar', mode='r') as file:
    print([m.name for m in file.getmembers()])
    
print('adding index.rst')
with tarfile.open('tarfile_append.tar', mode='a') as file:
    file.add('index.rst')
    
print('contents -> ')
with tarfile.open('tarfile_append.tar', mode='r') as file:
    print([m.name for m in file.getmembers()])