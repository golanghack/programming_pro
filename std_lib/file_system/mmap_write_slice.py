#! /usr/bin/env python3 

import mmap 
import shutil

# copy file 
shutil.copyfile('seed_data.txt', 'seed_data_copy.txt')

word = b'consectetuer'
reversed_ = word[::-1]
print('Looking for -> ', word)
print('Replacing with -> ', reversed_)

with open('seed_data_copy.txt', 'r+') as file_:
    with mmap.mmap(file_.fileno(), 0) as mmap_file:
        print(f'Before -> \n{mmap_file.readline().rstrip()}')
        # move to begin
        mmap_file.seek(0)
        
        location_word = mmap_file.find(word)
        mmap_file[location_word:(location_word + len(word))] = reversed_# ERROR
        mmap_file.flush()
        
        # move to begin 
        mmap_file.seek(0)
        print(f'After -> \n{mmap_file.readline().rstrip()}')
        
        # move to begin
        file_.seek(0)
        print(f'File -> \n{file_.readline().rstrip()}')

