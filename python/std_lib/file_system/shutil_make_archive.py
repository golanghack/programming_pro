#! /usr/bin/env python3

import logging 
import shutil
import sys 
import tarfile

logging.basicConfig(
    format='%(message)s', 
    stream=sys.stdout, 
    level=logging.DEBUG,
)
logger = logging.getLogger('pymotw')

print('Creating archive -> ')
shutil.make_archive('example', 'gztar', root_dir='..', base_dir='file_system', logger=logger,)

print('\nArchive contents -> ')
with tarfile.open('example.tar.gz', 'r', encoding='utf-8') as tar:
    for n in tar.getnames():
        print(n)