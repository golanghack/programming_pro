#! /usr/bin/env python3 

import os 

def disk_usage(path: str) -> float:
    """Return the number of bytes user by a file/foler and any descendents"""

    # direct usage
    total = os. path.getsize(path)
    # if this dir
    if os.path.isdir(path):
        for filename in os.listdir(path):
            child_path = os.path.join(path, filename)
            # add child`s usage to total
            total += disk_usage(child_path)
    print(f'{total:<7}', path)
    return total