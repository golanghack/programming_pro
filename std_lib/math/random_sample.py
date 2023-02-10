#! /usr/bin/env python3 

import random 

with open('/usr/share/dict/words', 'rt') as file:
    words = file.readlines()

words = [w.rstrip() for w in words]

for w in random.sample(words, 15):
    print(w)