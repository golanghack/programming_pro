#! /usr/bin/env python3 

import pickle
from CellPhone import CellPhone

FILENAME = 'cellpones.txt'

EOF = False
input_file = open(FILENAME, 'rb')
while not EOF:
    try:
        phone = pickle.load(input_file)
        print(phone.get_manufact())
        print(phone.get_model())
        print(phone.get_price())
    except EOFError as err:
        print(f'ERR -> {err}')
        EOF = True
input_file.close()