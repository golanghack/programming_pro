#! /usr/bin/env python3

import gzip 
import io 
import os 
import hashlib 

def get_hash(data):
    return hashlib.md5(data).hexdigest()

data = open('lorem.txt', 'r').read() * 1024

cksum = get_hash(data.encode('utf-8')) 

print('Level  Size       Checksum')
print('-----  ---------  -------------------------------')
print(f'data {data:>10} {cksum}')

for i in range(0, 10):
    filename = f'compress-level-{i}.gz'
    with gzip.open(filename, 'wb', compresslevel=i) as out:
        with io.TextIOWrapper(out, encoding='utf-8') as enc:
            enc.write(data)
    size = os.stat(filename).st_size
    cksum = get_hash(open(filename, 'rb').read())
    print(f'{i:>5d} {size:>10d} {cksum}')
