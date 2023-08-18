#! /usr/bin/env python3

from timetrials import timetrials as trial
from duplicates_version_1 import dup

def main() -> None:
    for n_range in [50, 100, 400, 800, 1600, 3200, 6400]:
        trial(dup, n_range)
        
if __name__ == '__main__':
    main()