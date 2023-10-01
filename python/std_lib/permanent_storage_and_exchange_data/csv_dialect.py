#! /usr/bin/env python3 

import csv

csv.register_dialect('pipes', delimiter='|')

with open('testdata.pipes', 'r', encoding='utf-8') as file_:
    reader = csv.reader(file_, dialect='pipes')
    for row in reader:
        print(row)