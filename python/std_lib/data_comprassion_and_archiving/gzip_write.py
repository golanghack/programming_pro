#! /usr/bin/env python3 

import gzip 
import io 
import os 

outfilename = 'example.txt.gz'

with gzip.open(outfilename, 'wb') as output_file:
    with io.TextIOWrapper(output_file, encoding='utf-8') as enc:
        enc.write('Contents of the example file go here.\n')
        
print(outfilename, 'contains', os.stat(outfilename).st_size, 'bytes')
os.system(f'file -b --mine {outfilename}')