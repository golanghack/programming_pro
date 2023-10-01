#! /usr/bin/env python3 

import bz2
import os 

data = 'Character with an accent'

with bz2.open('exapmle.bz2', 'wt', encoding='utf-8') as output_file:
    output_file.write(data)
    
with bz2.open('example.bz2', 'rt', encoding='utf-8') as input_file:
    print(f'Full file -> {input_file.read()}')
    
# move to begin 
with bz2.open('example.bz2', 'rt', encoding='utf-8') as input_file:
    input_file.seek(18)
    print(f'One character -> {input_file.read(1)}')
    
# move to in middle 
with bz2.open('example.bz2', 'rt', encoding='utf-8') as input_file:
    input_file.seek(19)
    try:
        print(input_file.read(1))
    except UnicodeDecodeError:
        print('ERROR -> failed to decode')