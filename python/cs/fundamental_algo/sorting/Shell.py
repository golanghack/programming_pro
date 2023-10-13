#! /usr/bin/env python3 

def shell_sort(massive : list) -> list:
    """ 
    >>> massive = [2, 3, 1]
    >>> shell_sort(massive)
    [1, 2, 3]
    """ 

    distance = len(massive) // 2
    while distance > 0:
        for i in range(distance, len(massive)):
            temp = massive[i]
            j = i 
            # sub list
            while j >= distance and massive[j - distance] > temp:
                massive[j] = massive[j - distance]
                j = j - distance
            massive[j] = temp
        # down distance for next elem
        distance = distance // 2
    return massive


if __name__ == '__main__':
    import doctest
    doctest.testmod()