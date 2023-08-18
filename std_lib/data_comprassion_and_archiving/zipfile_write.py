#! /usr/bin/env python3 

from zipfile_infolist import print_info
import zipfile

print('___CREATING ARCHIVE___')
with zipfile.ZipFile('write.zip', mode='w') as file:
    print('adding README.txt')
    file.write('README.txt')
    
print()
print_info('write.zip')