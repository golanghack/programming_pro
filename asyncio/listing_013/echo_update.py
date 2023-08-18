#! /usr/bin/env python3 

from random import randrange
import time

user_input = ''

while user_input != 'quit':
    user_input = input('Enter text -> ')
    for i in range(randrange(10)):
        time.sleep(.5)
        print(user_input)
