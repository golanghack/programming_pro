#! /usr/bin/env python3 

import signal
import threading
import os 
import time

def signal_handler(num, stack):
    print(f'Received signal {num} in {threading.currentThread().name}')

signal.signal(signal.SIGUSR1, signal_handler)

def wait_for_signal():
    print('Waiting for signal in', threading.currentThread().name)
    signal.pause()
    print('Done waiting')

# start threading for signals
reciever = threading.Thread(target=wait_for_signal, name='receiver',)
reciever.start()
time.sleep(.1)

def send_signal():
    print('sending signal in ', threading.currentThread().name)
    os.kill(os.getpid(), signal.SIGUSR1)

sender = threading.Thread(target=send_signal, name='sender')
sender.start()
sender.join()

# waiting signal 
print('Waitong for ', reciever.name)
signal.alarm(2)
reciever.join()