#! /usr/bin/env python3

"""<--MAGIC SQUARE-->"""

luoshu = [
          [4, 9, 2], 
          [3, 5, 7],
          [8, 1, 6]
          ]

def verification_magic_square(square):
    """This function trying find summs of all rows and columns and testing the same"""
    
    sums = []
    
    row_sums = [sum(square[i]) for i in range(0, len(square))]
    sums.append(row_sums)
    
    col_sums = [sum([row[i] for row in square]) for i in range(0, len(square))]
    sums.append(col_sums)
    
    main_diagonal = sum([square[i][i] for i in range(0, len(square))])
    sums.append([main_diagonal])
    
    anti_diagonal = sum([square[i][len(square) -1 - i] for i in range(0, len(square))])
    sums.append([anti_diagonal])
    
    flattened = [j for i in sums for j in i]
    return (len(list(set(flattened))) == 1)

print(verification_magic_square(luoshu))
    