#! /usr/bin/env python3 

import tarfile

print('___CREATING ARCHIVE___')

with tarfile.open('tarfile_addfile.tar', mode='w') as file:
    print('adding READMY.txt as RENAMED.txt')
    info = file.gettarinfo('README.txt', arcname='RENAMED.txt')
    file.addfile(info)
    
print()
print('Contents -> ')

with tarfile.open('tarfile_addfile.tar', mode='r') as file:
    for member_info in file.getmembers():
        print(member_info.name)