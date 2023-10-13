#! /usr/bin/env python3 

import asyncio
import concurrent.futures
import functools
import time 
from typing import Dict, List

def partition(data: List, parts_size: int) -> List:
    """Partition dataset on parts."""
    
    for i in range(0, len(data), parts_size):
        yield data[i:i + parts_size]
        
def map_frequencies(part: List[str]) -> Dict[str, int]:
    """Mapping data set."""
    
    counter = {}
    for line in part:
        word, _, count, _ = line.split('\t')
        if counter.get(word):
            counter[word] = counter[word] + int(count)
        else:
            counter[word] = int(count)
    return counter

def merging(first: Dict[str, int], second: Dict[str, int]) -> Dict[str, int]:
    """Merging parts of dataset"""
    
    merged = first
    for key in second:
        if key in merged:
            merged[key] = merged[key] + second[key]
        else:
            merged[key] = second[key]
    return merged

async def reduce(loop, pool, counters, part_size) -> Dict[str, int]:
    parts: List[List[Dict]] = list(partition(counters, part_size)) # one
    reducers = []
    
    while len(parts[0]) > 1:
        for part in parts:
            reducer = functools.partial(functools.reduce, merging, part) # two
            reducers.append(loop.run_in_executor(pool, reducer))
        reducer_parts = await asyncio.gather(*reducers) # three
        parts = list(partition(reducer_parts, part_size)) # foo
        reducers.clear()
    return parts[0][0]

async def main(part_size: int) -> None:
    with open('googlebooks-eng-all-1gram-20120701-a', encoding='utf-8') as f:
        contents = f.readlines()
        loop = asyncio.get_running_loop()
        tasks = []
        with concurrent.futures.ProcessPoolExecutor() as pool:
            start = time.time()
            
            for part in partition(contents, part_size):
                tasks.append(loop.run_in_executor(pool, functools.partial(map_frequencies, part)))
                intermediate_results = await asyncio.gather(*tasks)
                final_results = await reduce(loop, pool, intermediate_results, 500)
                
                print(f'Aardvark has appared {final_results["Aardvark"]} times.')
                end = time.time()
                print(f'MapReduce took -> {(end - start):.4f} seconds.')
                
if __name__ == '__main__':
    asyncio.run(main(part_size=60000))