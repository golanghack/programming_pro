#! /usr/bin/env python3 

import io 
import tarfile

text = 'This is the data to write to the archive'
data = text.encode('utf-8')

with tarfile.open('addfile_string.tar', mode='w') as file:
    info = tarfile.TarInfo('made_up_file.txt')
    info.size = len(data)
    file.addfile(info, io.BytesIO(data))
    
print('Contents -> ')
with tarfile.open('addfile_string.tar', mode='r') as file:
    for member_info in file.getmembers():
        print(member_info.name)
        f = file.extractfile(member_info)
        print(f.read().decode('utf-8'))
