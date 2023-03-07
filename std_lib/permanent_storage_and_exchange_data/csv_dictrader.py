#! /usr/bin/env python3 

import csv 
import sys 

with open(sys.argv[1], 'rt', encoding='utf-8') as file_:
    reader = csv.DictReader(file_)
    for row in reader:
        print(row)