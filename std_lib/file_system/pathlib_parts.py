#! /usr/bin/env python3 

import pathlib

path = pathlib.PurePosixPath('/usr/local')
print(path.parts)