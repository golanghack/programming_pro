#! /usr/bin/env python3 

from typing import List


def get_max(sequence: List[int]) -> int:
    """Return max value."""

    max_value = max(sequence)
    return max_value

def get_min(sequence: List[int]) -> int:
    """Return min value.""" 

    min_value = min(sequence)
    return min_value


def main():

    sequence = [i for i in range(14)]
    max_result = get_max(sequence)
    min_result = get_min(sequence)

    print(f'Maximum value -> {max_result}')
    print(f'Minimum value -> {min_result}')


if __name__ == '__main__':
    main()