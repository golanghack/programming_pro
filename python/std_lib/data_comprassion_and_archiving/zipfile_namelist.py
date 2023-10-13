#! /usr/bin/env python3 

import zipfile

with zipfile.ZipFile('example.zip', 'r') as z_file:
    print(z_file.namelist())