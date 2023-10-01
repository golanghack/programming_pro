#! /usr/bin/env python3 

import dbm 

with dbm.open('/tmp/exmple.db', 'w') as db:
    try:
        db[1] = 'one'
    except TypeError as err:
        print(err)