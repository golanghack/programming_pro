#! /usr/bin/env python3 

import signal
import os 
import time 

def do_exit(sig, stack):
    raise SystemExit('Exiting')

signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGUSR1, do_exit)

print('MY PID -> ', os.getpid())

signal.pause()