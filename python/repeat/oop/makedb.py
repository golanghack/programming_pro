#! /usr/bin/env python3 

from person import Person, Manager
import shelve

bob = Person('Bob')
sue = Person('Sue', job='dev', pay=100000)
tom = Manager('Tom', 5000.0)

db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()