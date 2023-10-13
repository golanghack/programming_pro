#! /usr/bin/env python3 

import os
import sys 
import subprocess
import time 


message = 'Programm -> '
filename = input(message)


def open_file(filename: str):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])



def forced_termination(process_name: str) -> None:
    try:
        time.sleep(10)
        os.system('taskkill /IM "' + process_name + '" /F')
    except TimeoutError as err:
        print(err)

