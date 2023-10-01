#! /usr/bin/env python3 

import hashlib

print(f'Guaranteed -> \n{", ".join(sorted(hashlib.algorithms_guaranteed))}\n')
print(f'Available -> \n {", ".join(sorted(hashlib.algorithms_available))}')