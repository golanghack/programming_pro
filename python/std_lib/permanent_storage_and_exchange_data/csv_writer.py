#! /usr/bin/env python3 

import csv 
import sys 

unicode_chars = '൹൹൹'

with open(sys.argv[1], 'wt', encoding='utf-8') as file_:
    writer = csv.writer(file_)
    writer.writerow(('Title 1', 'Title2', 'Title 3', 'Title 4'))
    
    for i in range(3):
        row = (
            i + 1, 
            chr(ord('a') + i),
            f'09/{i + 1:02d}/09', 
            unicode_chars[i],
        )
        
        writer.writerow(row)
print(open(sys.argv[1], 'rt', encoding='utf-8').read())