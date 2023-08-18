#! /usr/bin/env python3 

sequence = [i for i in range(1000000)]

def largest(sequence: list) -> int:
    """return maximum from sequence"""
    try:
        my_maximum = sequence[0]
        for value in range(1, len(sequence)):
            if my_maximum < sequence[value]:
                my_maximum = sequence[value]
        return my_maximum
    except (ValueError, IndexError) as err:
        print(f'Your empty sequence into -> {err}')


print(largest(sequence))
