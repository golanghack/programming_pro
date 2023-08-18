#! /usr/bin/env python3 

import subprocess

try:
    subprocess.run(['false'], check=True)
except subprocess.CalledProcessError as err:
    print(f'ERROR -> {err}')