#! /usr/bin/env python3 

import bz2
import contextlib


with bz2.BZ2File('example.bz2', 'rb') as input_file:
    print('Entire file -> ')
    all_data = input_file.read()
    print(all_data)
    
    expected = all_data[5:15]
    
    # return to begin
    input_file.seek(0)
    
    #move to 5 bytes 
    input_file.seek(5)
    print('Starting at position 5 for 10 bytes -> ')
    partial = input_file.read(10)
    print()
    print(expected == partial)