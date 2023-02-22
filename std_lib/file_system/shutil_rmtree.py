#! /usr/bin/env python3

import glob 
import pprint
import shutil

print('BEFORE -> ')
pprint.pprint(glob.glob('/tmp/example/*'))

shutil.rmtree('/tmp/example')

print('\nAFTER -> ')
pprint.pprint(glob.glob('/tmp/example/*'))