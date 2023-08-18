#! /usr/bin/env python3 

import codecs
import encodings

def search_one(encoding):
    print('Search_one -> searching for -> ', encoding)
    return None

def search_two(encoding):
    print('Search_two ->  earching for -> ', encoding)
    return None

codecs.register(search_one)
codecs.register(search_two)

utf8 = codecs.lookup('utf-8')
print('UTF-8 -> ', utf8)

try:
    unknown = codecs.lookup('no-such-encoding')
except LookupError as err:
    print('ERROR -> ', err)