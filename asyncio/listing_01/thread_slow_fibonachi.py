#! /usr/bin/env python3 

import threading
import time

def print_fb(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    print(f'fib({number}) -> {fib(number)}')
        
def fibs_with_threads():
    fortieth_thread = threading.Thread(target=print_fb, args=(40,))
    forty_first_thread = threading.Thread(target=print_fb, args=(41,))
    
    fortieth_thread.start()
    forty_first_thread.start()
    
    fortieth_thread.join()
    forty_first_thread.join()
    
start_threads = time.time()

fibs_with_threads()

end_threads = time.time()

print(f'Multithreading timing -> {end_threads - start_threads:.4f} sec.')