#! /usr/bin/env python3 

import bz2 
import io 
import os 

data = open('lorem.txt', 'r', encoding='utf-8').read() * 1024
print(f'Input contains {len(data.encode("utf-8"))} bytes')

for i in range(1, 10):
    filename = f'comprtess-level-{i}.bz2'
    with bz2.BZ2File(filename, 'wb', compresslevel=i) as output:
        with io.TextIOWrapper(output, encoding='utf-8') as enc:
            enc.write(data)
    
    os.system(f'cksum {filename}')