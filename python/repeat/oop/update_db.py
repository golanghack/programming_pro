#! /usr/bin/env python3 

import shelve

db = shelve.open('persondb')

for key in sorted(db):
    print(key, '\t->', db[key])
sue = db['Sue']
sue.give_raise(0.10)
db['Sue'] = sue

db.close()