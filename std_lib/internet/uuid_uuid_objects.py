#! /usr/bin/env python3 

import uuid

def show(message: str, list_: list):
    print(message)
    for v in list_:
        print(' ', v)
    print()

input_values = [
    '6ff28c58-f187-11ed-90af-77e8c6192866',
    '6ff28c59-f187-11ed-90af-77e8c6192867',
    '6ff28c5a-f187-11ed-90af-77e8c6192868',
    '6ff28c5b-f187-11ed-90af-77e8c6192869',
]

show('input_values', input_values)
uuids = [uuid.UUID(s) for s in input_values]
show('converted to uuids', uuids)

uuids.sort()
show('sorted', uuids)
