#! /usr/bin/env python3 

from CustomFuture import CustomFuture

future = CustomFuture()
i = 0

while True:
    try:
        print('Testing future object')
        gen = future.__await__()
        gen.send(None)
        print('Future not ready')
        if i == 2:
            print('set future')
            future.set_result('Ready')
        i = i + 1
    except StopIteration as si:
        print(f'Mean -> {si.value}')
        