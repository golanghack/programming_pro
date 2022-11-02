#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--STATISTICS-->"""

import collections
import math
import sys 

Statustics = collections.namedtuple('Statistics', 'mean mode median std_dev')

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        print(f'usage --> {sys.argv[0]} file1, [file2 [... fileN]]')
    sys.exit()
    
    numbers = []
    frequencies = collections.defaultdict(int)
    for filename in sys.argv[1:]:
        read_data(filename, numbers, frequencies)
    if numbers:
        statistics = calculate_statistics(numbers, frequencies)
        print_results(len(numbers), statistics)
    else:
        print("no numbers found")

def read_data(filename, numbers, frequencies):
    with open(filename, encoding="ascii") as file:
        for lino, line in enumerate(file, start=1):
            for x in line.split():
                try:
                    number = float(x)
                    numbers.append(number)
                    frequencies[number] += 1
                except ValueError as err:
                    print("{filename}:{lino}:skipping {x}: {err}".format(**locals()))
                    
def calculate_statistics(numbers, frecuencies):
    mean = sum(numbers) / len(numbers)
    mode = calculate_mode(frecuencies, 3)
    median = calculate_std_dev(numbers, mean)
    return Statustics(mean, mode, median, std_dev)

def calculate_mode(frecuencies, maximum_modes):
    highest_frequency = max(frecuencies.values())
    mode = [number for number, frecuency in frecuencies.items()
            if frecuency == highest_frequency]
    if not (1 <= len(mode) <= maximum_modes):
        mode = None
    else:
        mode.sort()
    return mode

def calculate_median(numbers):
    numbers = sorted(numbers)
    middle = len(numbers) // 2 
    median = numbers[middle]
    if len(numbers) % 2 == 0:
        median = (median + numbers[middle - 1]) / 2
    return median

def calculate_std_dev(numbers, mean):
    total = 0
    
    for number in numbers:
        total += ((number - mean) ** 2)
    variance = total / (len(numbers) - 1) # n - 1
    return math.sqrt(variance)


def print_results(count, statistics):
    real = "9.2f"
    if statistics.mode is None:
        modeline = ""
    elif len(statistics.mode) == 1:
        modeline = "mode    = {0:{fmt}}\n".format(statistics.mode[0], fmt=real)
    else:
        modeline = ("mode    =[" + ", ".join(["{0:.2f}".format(m) for m in statistics.mode]) + "]\n")
        
    print("""\
        count = {0:.6}
        mean = {mean:{fmt}}
        median = {median:{fmt}}
        {1}\
        std. dev = {std_dev:{fmt}}""".format(count, modeline, fmt=real, **statistics._asdict()))

if __name__ == "__main__":
    main()