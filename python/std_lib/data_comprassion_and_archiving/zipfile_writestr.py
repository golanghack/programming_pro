#! /usr/bin/env python3 

from zipfile_infolist import print_info
import zipfile 

message = 'This is did not exist in a file.'
with zipfile.ZipFile('writestr.zip', 
                     mode='w', 
                     compression=zipfile.ZIP_DEFLATED,
                     ) as file:
    file.writestr('from_string.txt', message)
    
print_info('writestr.zip')

with zipfile.ZipFile('writestr.zip', 'r') as file:
    print(file.read('from_string.txt'))