#! /usr/bin/env  python3 

import hashlib
from hashlib_data import lorem

hash_for_lorem = hashlib.md5()
hash_for_lorem.update(lorem.encode('utf-8'))
print(hash_for_lorem.hexdigest())