#! /usr/bin/env python3 

from concurrent.futures import ProcessPoolExecutor
import functools
import asyncio
from multiprocessing import Value 
from typing import List, Dict
from parallel_MapReduce_and_pool_processes import partition, merging

map_progress: Value

def init(progress: Value):
    global map_progress
    map_progress = progress
    
def map_frequencies(part: List[str]) -> Dict[str, int]:
    counter = {}
    for line in part:
        word, _, count, _ = line.split('\t')
        if counter.get(word):
            counter[word] = counter[word] + int(count)
        else:
            counter[word] = int(count)
    with map_progress.get_lock():
        map_progress.value += 1
    return counter

async def progress_reporter(total_partitions: int):
    while map_progress.value < total_partitions:
        print(f'Finished tasks of mapping -> {map_progress.value}/{total_partitions}')
        await asyncio.sleep(1)

async def main(parts_size: int) -> None:
    global map_progress
    
    with open('googlebooks-eng-all-1gram-20120701-a', encoding='utf-8') as f:
        contents = f.readlines()
        loop = asyncio.get_running_loop()
        tasks = []
        map_progress = Value('i', 0)
        
        with ProcessPoolExecutor(initializer=init, 
                                 initargs=(map_progress,)) as pool:
            total_parts = len(contents) // parts_size
            reporter = asyncio.create_task(progress_reporter(total_parts))
            
            for part in partition(contents, parts_size):
                tasks.append(loop.run_in_executor(pool, functools.partial(map_frequencies, part)))

            counters = await asyncio.gather(*tasks)
            await reporter
            
            final_result = functools.reduce(merging, counters)
            
            print(f'Aardvark meets {final_result["Aardvark"]} times.')

if __name__ == '__main__':
    asyncio.run(main(parts_size=60000))