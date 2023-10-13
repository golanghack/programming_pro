#! /usr/bin/env python3

import threading

def hello_from_thread():
    print(f'Hello from thead -> {threading.current_thread()}!')
    
hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'Now Python make {total_threads} tread[`s]')
print(f'Name of current thread -> {thread_name}')
hello_thread.join()