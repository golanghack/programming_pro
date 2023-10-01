#! /usr/bin/env python3 

import filecmp
import os 

# find elements exists in both  directory
dir1_contents = set(os.listdir('example/dir1'))
dir2_contents = set(os.listdir('example/dir2'))

common = list(dir1_contents and dir2_contents)

common_files = [file_ for file_ in common if os.path.isfile(os.path.join('example/dir1', file_))]

print('Common files -> ', common_files)

# cmp directoryes
match, mismatch, errors = filecmp.cmpfiles('example/dir1', 'example/dir2', common_files,)

print('MATCH -> ', match)
print('MISMATCH -> ', mismatch)
print('ERRORS -> ', errors)