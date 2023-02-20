#! /usr/bin/env python3

import pathlib 
import time

my_path = pathlib.Path('touched')
if my_path.exists():
    print('already exists')
else:
    print('creating')
    
my_path.touch()

start = my_path.stat()
time.sleep(1)

my_path.touch()
end = my_path.stat()

print('Start -> ', time.ctime(start.st_mtime))
print('End -> ', time.ctime(end.st_mtime))

