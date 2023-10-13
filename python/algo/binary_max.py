#! /usr/bin/env python3 

sequence = [i for i in range(1000)]

def largest(sequence: list) -> set:
    """return two maximum from sequence"""
    try:
        first_max, second_max = sequence[:2]
        if first_max < second_max:
            first_max, second_max = second_max, first_max

            for value in range(2, len(sequence)):
                if first_max < sequence[value]:
                    first_max, second_max = sequence[value], first_max
                elif second_max < sequence[value]:
                    second_max = sequence[value]
            return (first_max, second_max)
    except (ValueError, IndexError) as err:
        print(f'{err}')

      