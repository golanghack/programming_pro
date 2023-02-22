#! /usr/bin/env python3 

import glob
import pprint
import shutil

def verbose_copy(src: str, dst: str) -> str:
    print(f'copying\n {src!r}\n to {dst!r}')
    return shutil.copy2(src, dst)

print('BEFORE -> ')
pprint.pprint(glob.glob('/tmp/example/*'))
print()

shutil.copytree(
    '../shutil', '/tmp/example', 
    copy_function=verbose_copy, 
    ignore=shutil.ignore_patterns('*.py'),
)

print('\nAFTER -> ')
pprint.pprint(glob.glob('/tmp/example/*'))
