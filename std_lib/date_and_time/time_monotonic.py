#! /usr/bin/env python3 

import time 

start = time.monotonic()
time.sleep(1)
end = time.monotonic()

print(f'start -> {start:>9.2f}')
print(f'end -> {end:>9.2f}')
print(f'span -> {(end - start):>9.2f}')