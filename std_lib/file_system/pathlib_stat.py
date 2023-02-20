#! /usr/bin/env python3 

import pathlib
import sys 
import time 

if len(sys.argv) == 1:
    filename = __file__
else:
    filename = sys.argv[1]
    
my_path = pathlib.Path(filename)
stat_info = my_path.stat()

# full stat
print(f'{filename}')
print('    Size -> ', stat_info.st_size)
print('    Permissions -> ', oct(stat_info.st_mode))
print('    Owner -> ', stat_info.st_uid)
print('    Device -> ', stat_info.st_dev)
print('    Created -> ', time.ctime(stat_info.st_ctime))
print('    Last modified -> ', time.ctime(stat_info.st_mtime))
print('    Last accessed -> ', time.ctime(stat_info.st_atime))