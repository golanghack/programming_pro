#! /usr/bin/env python3 

import random
import os 
import pickle 

if os.path.exists('state.dat'):
    # return earlier state
    print('Found state.dat, initializing random module')
    with open('state.dat', 'rb') as file:
        state = pickle.load(file)
    random.setstate(state)
    
else:
    # use begin state
    print('No state.dat, seeding')
    random.seed(1)

# create sporadic means
for i in range(3):
    print(f'{random.random():04.3f}', end=' ')
print()

# save state for next running
with open('state.dat', 'wb') as file:
    pickle.dump(random.getstate(), file)

# get adding sporadic means
print('\nAfter saving state -> ')
for i in range(3):
    print(f'{random.random():04.3f}')
print()