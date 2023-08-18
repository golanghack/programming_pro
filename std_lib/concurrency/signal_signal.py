#! /usr/bin/env python3 

import signal
import os 
import time 

def recieve_signal(signum, stack):
    print('Recieved -> ', signum)

# registration signal descriptors
signal.signal(signal.SIGUSR1, recieve_signal)
signal.signal(signal.SIGUSR2, recieve_signal)

# id process which will be use with kill
# for send signal to this program
print('My PID -> ', os.getpid())

while True:
    print('Wait')
    time.sleep(3)