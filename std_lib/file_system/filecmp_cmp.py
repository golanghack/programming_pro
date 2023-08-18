#! /usr/bin/env python3

import filecmp 

print('common_file -> ', end=' ')
print(filecmp.cmp('example/dir1/common_file', 'example/dir2/common_file'), end=' ')
print(filecmp.cmp('example/dir1/common_file', 'example/dir2/common_file', shallow=False))

print('not_the_same -> ', end=' ')
print(filecmp.cmp('example/dir1/not_the_same', 'example/dir2/not_the_same'), end=' ')
print(filecmp.cmp('example/dir1/not_the_same', 'example/dir2/not_the_same'), shallow=False)

