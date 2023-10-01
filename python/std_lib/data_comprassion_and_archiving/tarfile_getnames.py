#! /usr/bin/env python3 

import tarfile

with tarfile.open('example.tar', 'r') as file:
    print(file.getnames())