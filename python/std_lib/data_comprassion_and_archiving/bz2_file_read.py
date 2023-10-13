#! /usr/bin/env python3 

import bz2 
import io 

with bz2.BZ2File('example.bz2', 'rb') as input_file:
    with io.TextIOWrapper(input_file, encoding='utf-8') as dec:
        print(dec.read())