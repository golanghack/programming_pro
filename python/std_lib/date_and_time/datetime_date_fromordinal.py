#! /usr/bin/env python3 

import datetime 
import time

ordinal = 588114
print('ordinal ->', ordinal)
print('fromordinal(ordinal) -> ', datetime.date.fromordinal(ordinal))

t = time.time()
print('t -> ', t)
print('fromtimestamp(t) -> ', datetime.date.fromtimestamp(t))