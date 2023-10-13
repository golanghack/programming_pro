#! /usr/bin/env python3 

import os 
import signal
import subprocess
import tempfile
import time
import sys 

script = """
#! /bin/sh
echo "SHell script in process $$"
set -x 
python3 signal_child.py
"""

script_file = tempfile.NamedTemporaryFile('wt')
script_file.write(script)
script_file.flush()

proc = subprocess.Popen(['sh', 'script_file.name'])
print(f'PARENT -> Pausing before signaling {proc.pid}')
sys.stdout.flush()

time.sleep(1)
print(f'PARENT -> Signaling child -> {proc.pid}')
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)
time.sleep(3)
