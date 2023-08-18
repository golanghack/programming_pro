#! /usr/bin/env python3 

import subprocess

try:
    completed = subprocess.run(
        'echo to stdout; echo to stderr 1>&2; exit 1', 
        check=True, 
        shell=True, 
        stdout=subprocess.PIPE,
    )
except subprocess.CalledProcessError as err:
    print(f'ERROR -> {err}')

else:
    print('return -> ', completed.returncode)
    print(f'Have {len(completed.stdout)} bytes in stdout -> {completed.stdout.decode("utf-8")}')