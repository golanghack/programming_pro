#! /usr/bin/env python3 

import signal 
import time 

def receive_alarm(signum, stack):
    print('Alarm -> ', time.ctime())

# call recieve_alarm acros 2 sec
signal.signal(signal.SIGALRM, receive_alarm)
signal.alarm(2)

print('Before -> ', time.ctime())
time.sleep(4)
print('After -> ', time.ctime())