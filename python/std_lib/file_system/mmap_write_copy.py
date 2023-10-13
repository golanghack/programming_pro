#! /usr/bin/env python3 

import mmap 
import shutil

# copy file 
shutil.copyfile('seed_data.txt', 'seed_data_copy.txt')

word = b'consectetuer'
reversed_ = word[::-1]

with open('seed_data_copy.txt', 'r+', encoding='utf-8') as file_:
    with mmap.mmap(file_.fileno(), 0, access=mmap.ACCESS_COPY) as mmap_file:
        print(f'Memory Before -> \n{mmap_file.readline().rstrip()}')
        print(f'File Before -> \n{file_.readline().rstrip()}')
        
        # move to begin 
        mmap_file.seek(0)
        location_word = mmap_file.find(word)
        mmap_file[location_word: location_word + len(word)] = reversed_
        
        # move to begin 
        mmap_file.seek(0)
        print(f'Memory After -> {mmap_file.readline().rstrip()}')
        
        file_.seek(0)
        print(f'File After -> \n{file_.readline().rstrip()}')