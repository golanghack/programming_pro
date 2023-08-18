#! /usr/bin/env python3 

import subprocess

completed = subprocess.run('echo $HOME', shell=True)
print('return -> ', completed.returncode)