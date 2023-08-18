#! /usr/bin/env python3 

from zipfile_infolist import print_info
import zipfile

print('__CREATING ARCHIVE___')
with zipfile.ZipFile('append.zip', mode='w') as file:
    file.write('README.txt')
    
print()
print_info('append.zip')

print('appending to the archive')
with zipfile.ZipFile('append.zip', mode='a') as file:
    file.write('README.txt', arcname='README@.txt')
    
print()
print_info('append.zip')