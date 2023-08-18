#! /usr/bin/env python3 

import pickle
from CellPhone import CellPhone

FILENAME = 'cellpones.txt'
mark = 'Kia'
mod = '1222K'
price = 100000.000

out_file = open(FILENAME, 'wb')
phone = CellPhone(mark, mod, price)
pickle.dump(phone, out_file)
out_file.close()

print(f'Data in {FILENAME} file')