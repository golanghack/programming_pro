#! /usr/bin/env python3 

import glob

print('Named explicitly ->')
for name in sorted(glob.glob('dir/subdir/*')):
    print(f' {name}')
    
print('Named with wildcard -> ')
for name in sorted(glob.glob('dir/*/*')):
    print(f'  {name}')