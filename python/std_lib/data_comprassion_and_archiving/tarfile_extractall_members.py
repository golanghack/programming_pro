#! /usr/bin/env python3 

import tarfile
import os 

os.mkdir('outdir')
with tarfile.open('example.tar', 'r') as file:
    file.extractall('outdir', members=[file.getmember('READMY.txt')],)
print(os.listdir('outdir'))