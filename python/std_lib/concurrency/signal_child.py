#! /usr/bin/env python3

import os 
import signal 
import time
import sys 

pid = os.getpid()
received = False

def signal_usr1(signum, frame):
    """Callback request from signal"""

    global received
    received = True

    print(f'CHILD -> {pid:>6} -> Recieved USR1')
    sys.stdout.flush()

print(f'CHILD -> {pid:>6} -> setting up signal handler')
sys.stdout.flush()
signal.signal(signal.SIGUSR1, signal_usr1)

print(f'CHILD -> {pid:>6} pausing to wait fo signal')
sys.stdout.flush()
time.sleep(3)

if not received:
    print(f'CHILD -> {pid:>6} Never recieved signal ')