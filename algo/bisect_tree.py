#! /usr/bin/env python3 

def bisect_tree(sequence: list) -> set:
    """return largest int in list and less one number""" 

    lenght = len(sequence)
    universal_multiple = (lenght - 1)
    largest = [None] * universal_multiple
    lowest = [None] * universal_multiple
    # start list -> -1
    middle = [-1] * universal_multiple

    index = 0
    # bisect in list
    for i in range(0, lenght, 2):
        if sequence[i] < sequence[i + 1]:
            largest[index] = sequence[i + 1]
            lowest[index] = sequence[i]
        else:
            largest[index] = sequence[i]
            lowest[index] = sequence[i + 1]
        index += 1
    
    number_of_position = 0
    while index < lenght - 1:
        if largest[number_of_position] < largest[number_of_position + 1]:
            largest[index] = largest[number_of_position + 1]
            lowest[index] = largest[number_of_position]
            middle[index] = number_of_position + 1 
        else:
            largest[index] = largest[number_of_position]
            lowest[index] = largest[number_of_position + 1]
            middle[index] = number_of_position
        number_of_position += 2
        index += 1
    
    most_large = largest[number_of_position]
    second = lowest[number_of_position]
    mid = middle[number_of_position]
    while mid >= 0:
        if second < lowest[mid]:
            second = lowest[mid]
        mid = middle[mid]

    return (most_large, second)

sequence = [1, 2, 3, 4, 5, 6]

print(bisect_tree(sequence))