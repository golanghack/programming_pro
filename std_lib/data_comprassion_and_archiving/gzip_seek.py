#! /usr/bin/env python3 

import gzip

with gzip.open('example.txt.gz', 'rb') as input_file:
    print('Entire file -> ')
    all_data = input_file.read()
    print(all_data)
    
    expected = all_data[5:15]
    
    # move to begin 
    input_file.seek(0)
    
    # move to forward on 5 bytes 
    input_file.seek(5)
    print('Starting at position 5 for 10 bytes -> ')
    partial = input_file.read(10)
    print(partial)
    
    print()
    print(expected == partial)