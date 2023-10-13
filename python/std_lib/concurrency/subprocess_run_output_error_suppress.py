#! /usr/bin/env python3 

import subprocess

try:
    completed = subprocess.run(
        'echo to stdout; echo to stderr 1>&2; exit 1', 
        shell=True, 
        stdout=subprocess.DEVNULL, 
        stderr=subprocess.DEVNULL,
    )

except subprocess.CalledProcessError as err:
    print(f'ERROR -> {err}')

else:
    print('return -> ', completed.returncode)
    print(f'stdout is {completed.stdout!r}')
    print(f'stderr is {completed.stderr!r}')