#! /usr/bin/env python3 

import pathlib

home = pathlib.Path.home()
print('Home -> ', home)

cwd = pathlib.Path.cwd()
print('cwd -> ', cwd)
