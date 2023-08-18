#! /usr/bin/env python3 

import collections
import threading
import time

candle = collections.deque(range(5))

def burn(direction, next_source):
    """The burn time returned."""
    
    while True:
        try:
            next_ = next_source()
        except IndexError:
            break
        else:
            print(f'{direction:>8} -> {next_}')
            time.sleep(0.1)

    print(f'{direction:>8} done')
    return

left = threading.Thread(target=burn, args=('Left', candle.popleft))
right = threading.Thread(target=burn, args=('Right', candle.pop))

left.start()
right.start()
left.join()
right.join()        