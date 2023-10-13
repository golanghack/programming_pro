#! /usr/bin/env python3 

"""Problem realisation serach max in sequence""" 

my_seq = [i for i in range(1000)]

def flawed(sequence: list) -> int:
    """Bad realisation max function""" 

    # current maximmum
    my_maximum = 0 
    for value in sequence:
        if my_maximum < value:
            my_maximum = value
    return my_maximum

print(flawed(my_seq))