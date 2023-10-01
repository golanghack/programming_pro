#! /usr/bin/env python3 

import random
import time 

print('Default initialization -> \n')

r1 = random.SystemRandom()
r2 = random.SystemRandom()

for i in range(3):
    print(f'{r1.random():04.3f} {r2.random():04.3f}')
    
print('\nSame seed -> \n')

seed = time.time()
r1 = random.SystemRandom(seed)
r2 = random.SystemRandom(seed)

for i in range(3):
    print(f'{r1.random():04.3f} {r2.random():04.3f}')