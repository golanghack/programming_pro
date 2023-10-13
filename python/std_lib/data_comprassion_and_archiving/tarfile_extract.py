#! /usr/bin/env python3 

import tarfile
import os 

os.mkdir('outdir')
with tarfile.open('example.tar', 'r') as file:
    file.extract('README.txt', 'outdir')

print(os.listdir('outdir'))