#! /usr/bin/env python3 

import glob 
import shutil

print('BEFORE -> ', glob.glob('shutil_copifile.*'))
shutil.copyfile('shutil_copyfile.py', 'shutil_copyfile.py.copy')

print('AFTER -> ', glob.glob('shutil_copyfile.*'))