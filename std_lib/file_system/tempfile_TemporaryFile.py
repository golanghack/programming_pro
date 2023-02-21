#! /usr/bin/env python3 

import os 
import tempfile

print('Building a filename with PID -> ')
filename = f'/tmp/my_name.{os.getpid()}.txt'

with open(filename, 'w+b') as temp:
    print('temp -> ')
    print(f'{temp!r}')
    print('temp.name -> ')
    print(f'  {temp.name!r}')
    
# handle removed tempfile
os.remove(filename)

print()
print('TemporaryFile -> ')
with tempfile.TemporaryFile() as temp:
    print('temp -> ')
    print(f'  {temp!r}')
    print('temp.name -> ')
    print(f'  {temp.name!r}')