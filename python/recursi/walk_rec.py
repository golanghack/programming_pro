#!/usr/bin/env python3

import os

def do_recode(path):
    if os.path.isdir(path) == 1 :
        print ("Processing " + path)
        for file in os.listdir(path):
            do_recode(path+"/"+file)
    else :
        filename = os.path.basename(path)
        filenameparts = filename.split(".")
print(do_recode('../'))