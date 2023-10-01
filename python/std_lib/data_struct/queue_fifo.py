#! /usr/bin/env python3 

import queue

queue_std = queue.Queue()

for i in range(5):
    queue_std.put(i)
    
while not queue_std.empty():
    print(queue_std.get(), end=' ')
print()