#! /usr/bin/env python3 

import hashlib
from hashlib_data import lorem

lorem_hash = hashlib.sha1()
lorem_hash.update(lorem.encode('utf-8'))
print(lorem_hash.hexdigest())