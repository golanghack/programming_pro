#! /usr/bin/env python3 

sequence = [i for i in range(1000)]

def alter_max(sequence: list) -> int:
    """return maximum from sequence"""

    for one in sequence:
        for two in sequence:
            if one < two:
                break
        else:
            return one
    return None

