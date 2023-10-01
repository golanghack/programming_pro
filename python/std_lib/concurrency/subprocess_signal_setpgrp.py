#! /usr/bin/env python3 

import os 
import signal
import subprocess
import tempfile
import time
import sys 

def show_setting_prgrp():
    print(f'Calling os.setpgrp() frm {os.getpid()}')
    os.setpgrp()
    print(f'Process group is now {os.getpid(), os.getpgrp()}')
    sys.stdout.flush()

script = ''' 
#! /bin/sh 
echo "Shell script in process $$"
set -x 
python3 signal_child.py
'''

script_file = tempfile.NamedTemporaryFile('wt')
script_file.write(script)
script_file.flush()

proc = subprocess.Popen(['sh', script_file.name], preexec_fn=show_setting_prgrp,)

print(f'PARENT Pausing before signaling {proc.pid}')
sys.stdout.flush()
time.sleep(1)

print(f'PARENT -> Signaling process group {proc.pid}')
sys.stdout.flush()
os.killpg(proc.pid, signal.SIGUSR1)
time.sleep(3)