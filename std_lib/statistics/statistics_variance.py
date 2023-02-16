#! /usr/bin/env python3 

from statistics import * 
import subprocess

def get_line_lenghts() -> None:
    """Getting lens and analizyng lenghts."""
    
    cmd = 'wc -l ../[a-z]*/*.py'
    out = subprocess.check_output(cmd, shell=True).decode('utf-8')
    
    for line in out.splitlines():
        parts = line.split()
        if parts[1].strip().lower() == 'total':
            break
        
        nlines = int(parts[0].strip())
        if not nlines:
            continue # scip empty files 
        yield (nlines, parts[1].strip())
        
data = list(get_line_lenghts())

lenghts = [d[0] for d in data]
sample = lenghts[::2]

print('Basic statistics -> ')
print(f'Count -> {len(lenghts):3d}')
print(f'min -> {min(lenghts):6.2f}')
print(f'max -> {max(lenghts):6.2f}')
print(f'mean -> {mean(lenghts):6.2f}')

print('\nPopulation variance -> ')
print(f'pstdev -> {pstdev(lenghts):6.2f}')
print(f'pvariance -> {pvariance(lenghts):6.2f}')

print('\nEstimated variance for sample -> ')
print(f'count -> {len(sample):3d}')
print(f'stdev -> {stdev(lenghts):6.2f}')
print(f'variance -> {variance(sample):6.2f}')