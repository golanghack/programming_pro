#! /usr/bin/env python3

import decimal 
import threading
from queue import PriorityQueue

class Multiplier(threading.Thread):
    """Multiplier."""
    
    def __init__(self, a: int, b: int, prec: int, q: PriorityQueue) -> None:
        self.a = a 
        self.b = b 
        self.prec = prec
        self.q = q 
        threading.Thread.__init__(self)
        
    def run(self) -> None:
        context = decimal.getcontext().copy()
        context.prec
        decimal.setcontext(context)
        self.q.put((self.prec, self.a * self.b))
        
a = decimal.Decimal('3.14')
b = decimal.Decimal('1.234')

# object PriorityQueue return sorted on prec independent from threads
q = PriorityQueue()
threads = [Multiplier(a, b, i, q) for i in range(1, 6)]
for t in threads:
    t.start()
for t in threads:
    t.join()
    
for i in range(5):
    prec, value = q.get()
    print(f'{prec}  {value}')