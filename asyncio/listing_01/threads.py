#! /usr/bin/env python3 

import os
import threading

print(f'Do Python-process with id -> {os.getpid()}')

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'Now Python make {total_threads} tread[`s]')
print(f'Name current thread -> {thread_name}')