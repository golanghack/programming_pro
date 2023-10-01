#! /usr/bin/env python3 

import mmap 
import re 

pattern = re.compile(rb'(\.\W+)?([^.]?lorem[^.]*?\.)', re.DOTALL | re.IGNORECASE | re.MULTILINE)

with open('seed_data.txt', 'r', encoding='utf-8') as file_:
    with mmap.mmap(file_.fileno(), 0, access=mmap.ACCESS_READ) as mm_file:
        for match in pattern.findall(mm_file):
            print(match[1].replace(b'\n', b' '))
