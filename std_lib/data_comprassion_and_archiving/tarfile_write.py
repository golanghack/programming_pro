#! /usr/bin/env python3 

import tarfile

print('___CREATING ARCHIVE___')
with tarfile.open('tarfile_add.tar', mode='w') as file:
    print('Adding READMY.txt')
    file.add('READMY.txt')
    
print()
print('Contents -> ')
with tarfile.open('tarfile_add.tar', mode='r') as file:
    for member_info in file.getmembers():
        print(member_info.name)