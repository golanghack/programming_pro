#! /usr/bin/env python3 

import multiprocessing
import multiprocessing_import_worker

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        process = multiprocessing.Process(target=multiprocessing_import_worker.worker, )
        jobs.append(process)
        process.start()

