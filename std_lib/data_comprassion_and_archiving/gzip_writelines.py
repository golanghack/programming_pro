#! /usr/bin/env python3 

import gzip 
import io 
import itertools
import os 


with gzip.open('example_lines.txt.gzip', 'wb') as out:
    with io.TextIOWrapper(out, encoding='utf-8') as enc:
        enc.writelines(itertools.repeat('The same line\n', 10))
os.system('gzcat example_lines.txt.gz')