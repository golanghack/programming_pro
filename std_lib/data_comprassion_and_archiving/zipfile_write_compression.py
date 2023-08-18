#! /usr/bin/env python3 

from zipfile_infolist import print_info
import zipfile

try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED
    
modes = {
    zipfile.ZIP_DEFLATED: 'deflated', 
    zipfile.ZIP_STORED: 'stored',
}

print('___CREATING ARCHIVE___')
with zipfile.ZipFile('write_compressions.zip', mode='w') as file:
    mode_name = modes[compression]
    print('adding README.txt with compression mode ', mode_name)
    file.write('README.txt', compress_type=compression)
    
print()
print_info('write_compression.zip')