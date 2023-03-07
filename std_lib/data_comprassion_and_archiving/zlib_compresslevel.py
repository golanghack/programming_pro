#! /usr/bin/env python3 

import zlib 

input_ = b'Some repeated text.\n' * 1024 
template = '{:>5} {:>5}'

print(template.format('Level', 'Size'))
print(template.format('-----', '-----'))

for i in range(0, 10):
    data = zlib.compress(input_, i)
    print(template.format(i, len(data)))