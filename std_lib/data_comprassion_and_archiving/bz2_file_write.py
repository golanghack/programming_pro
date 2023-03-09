#! /usr/bin/env python3 

import bz2 
import io 
import os 

data = 'Contents of the example fale go here.\n'

with bz2.BZ2File('example.bz2', 'wb') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as enc:
        enc.write(data)
        
os.system('file example.bz2')