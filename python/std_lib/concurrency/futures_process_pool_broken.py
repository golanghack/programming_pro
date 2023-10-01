#! /usr/bin/env python3 

from concurrent import futures
import os 
import signal

with futures.ProcessPoolExecutor(max_workers=2) as ex:
    print('getting the pid for one worker')
    func_1 = ex.submit(os.getpid)
    pid_1 = func_1.result()

    print(f'killing process {pid_1}')
    os.kill(pid_1, signal.SIGHUP)

    print('submitting anither task')
    func_2 = ex.submit(os.getpid) 
    try:
        pid_2 = func_2.result()
    except futures.process.BrokenProcessPool() as err:
        print(f'could not start new tasks -> {err}')