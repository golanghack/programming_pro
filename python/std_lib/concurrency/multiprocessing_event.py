#! /usr/bin/env python3 

import multiprocessing
import time

def wait_for_event(event):
    """Wait event"""

    print('wait_for_event -> start')
    event.wait()
    print('wait_for_event -> event.is_set(), ', event.is_set())


def wait_for_event_timeout(event, timeout):
    """Wait timeout seconds"""

    print('wait_for_timeout -> starting')
    event.wait(timeout)
    print('wait_for_event_timeout -> event.is_set() ', event.is_set())

if __name__ == '__main__':
    event = multiprocessing.Event()
    process_1 = multiprocessing.Process(
        name='block', 
        target=wait_for_event, 
        args=(event, ),
    )

    process_2 = multiprocessing.Process(
        name='nonblock', 
        target=wait_for_event_timeout, 
        args=(event, 2),
    )

    process_2.start()

    print('main -> waiting before calling Event.set()')
    time.sleep(3)
    event.set()
    print('main -> event is set')

    