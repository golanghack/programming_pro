#! /usr/bin/env python3

import glob 

for name in sorted(glob.glob('dir/*')):
    print(name)