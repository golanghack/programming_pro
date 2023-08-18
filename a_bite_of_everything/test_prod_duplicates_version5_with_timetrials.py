#! /usr/bin/env python3 

from duplicates_version_5 import dup
from timetrials import timetrials as trial 

for n_range in [50, 200, 400, 800, 1600, 3200, 6400]:
    trial(dup, n_range)