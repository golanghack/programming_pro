#! /usr/bin/env python3 

import tempfile

tempfile.tempdir = '/one/changed/this/path'
print('gettempdir() -> ', tempfile.gettempdir())
