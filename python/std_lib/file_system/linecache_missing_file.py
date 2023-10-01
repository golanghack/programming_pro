#! /usr/bin/env python3 

import linecache

# if module linecache dont find file error hide
no_such_file = linecache.getline('this_file_does_not_exist.txt', 1,)
print(f'NO FILE -> {no_such_file!r}')