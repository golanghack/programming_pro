#! /usr/bin/env python3 

import mmap

with open('seed_data.txt', 'r', encoding='utf-8') as file_:
    with mmap.mmap(file_.fileno(), 0, access=mmap.ACCESS_READ) as file_mmap:
        print('First 10 bytest via read -> ', file_mmap.read(10))
        print('First 10 bytes via slice -> ', file_mmap[:10])
        print('2nd 10 bytes via read -> ', file_mmap[10:])