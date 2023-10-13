#! /usr/bin/env python3 

import tarfile
import time 

with tarfile.open('example.tar', 'r') as file:
    for member_info in file.getmembers():
        print(member_info.name)
        print('  Modified -> ', time.ctime(member_info.mtime))
        print('  Mode     -> ', oct(member_info.mode))
        print('  Type     -> ', member_info.type)
        print('  Size     -> ', member_info.size, 'bytes')
        print()