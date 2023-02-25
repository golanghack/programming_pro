#! /usr/bin/env python3 

import codecs 
import sys 

encoding = sys.argv[1]
filename = encoding + '.txt'

print('Reading from', filename)
with codecs.open(filename, mode='r', encoding=encoding) as file_:
    print(repr(file_.read()))