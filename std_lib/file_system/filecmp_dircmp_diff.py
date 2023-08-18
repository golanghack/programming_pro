#! /usr/bin/env python3 

import filecmp

dc = filecmp.dircmp('example/dir1', 'example/dir2')

print('Same -> ', dc.same_files)
print('Diff -> ', dc.diff_files)
print('Funny-> ', dc.funny_files)
