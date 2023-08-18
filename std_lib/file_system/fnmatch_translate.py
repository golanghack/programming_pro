#! /usr/bin/env python3 

import fnmatch

pattern = 'fnmatch_*.py'
print('pattern -> ', pattern)
print('Regex -> ', fnmatch.translate(pattern))