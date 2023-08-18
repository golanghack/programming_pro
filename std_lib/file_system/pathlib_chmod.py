#! /usr/bin/env python3 

import os 
import pathlib 
import stat 

# creating test file 
test_file = pathlib.Path('pathlib_chmod_example.txt')

if test_file.exists():
    test_file.unlink()

test_file.write_text('my contents')

# description permissions with stat
existing_permissions = stat.S_IMODE(test_file.stat().st_mode)
print(f'Before -> {existing_permissions:o}')

# description method changes of permissions
if not(existing_permissions & os.X_OK):
    print('Adding execute permissions')
else:
    print('Removing execute permission')
    # use xor for take a bite for permission
    new_permissions = existing_permissions ^ stat.S_IXUSR
    test_file.chmod(new_permissions)
    
# change  and print
after_permissions = stat.S_IMODE(test_file.stat().st_mode)
print(f'After -> {after_permissions:o}')