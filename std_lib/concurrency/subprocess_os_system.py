#! /usr/bin/env python3 

import subprocess

completed = subprocess.run(['ls', '-1'])
print('return -> ', completed.returncode)
