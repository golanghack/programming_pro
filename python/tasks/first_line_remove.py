#! /bin/env python3 

import shutil

filename = 'file.txt'
source_file = open(filename, 'r')
source_file.readline()

#файл будет сжат так что нужно переименование 
target_file = open('file.txt.new', 'w')

shutil.copyfileobj(source_file, target_file)