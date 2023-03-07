#! /usr/bin/env python3 

import csv 
import sys 

fieldnames = ('Title 1', 'Title 2', 'Title 3', 'Title 4')

headers = {
    n: n
    for n in fieldnames
}

unicode_chars = '൹൹൹'

with open(sys.argv[1], 'wr', encoding='utf-8') as file_:
    writer = csv.DictWriter(file_, fieldnames=fieldnames)
    writer.writeheader()
    
    for i in range(3):
        writer.writerow({
            'Title 1': i + 1, 
            'Title 2': chr(ord('a') + i),
            'Title 3': f'09/{i + 1:02d}/23',
            'Title 4': unicode_chars[i],
        })
        
print(open(sys.argv[1], 'rt', encoding='utf-8').read())