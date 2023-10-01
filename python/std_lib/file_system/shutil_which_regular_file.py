#! /usr/bin/env python3 

import os 
import shutil

path = os.pathsep.join(['.', os.path.expanduser('~/pymotw'),])
mode = os.F_OK | os.R_OK

filename = shutil.which('config.ini', mode=mode, path=path,)

print(filename)