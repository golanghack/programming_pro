#! /usr/bin/env python3 

import csv
import pprint

def test_ratings():
    with open('series.csv', 'r', newline='') as file_:
        data = list(csv.reader(file_))
        pprint.pprint(data)