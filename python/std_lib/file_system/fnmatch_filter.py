#! /usr/bin/env python3 

import fnmatch
import os 
import pprint

pattern = 'fnmatch_*.py'
print('Pattern -> ', pattern)

files = os.listdir('.')

print('\nFiles -> ')
pprint.pprint(files)

print('\nMatches -> ')
pprint.pprint(fnmatch.filter(files, pattern))