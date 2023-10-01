#! /usr/bin/env python3 

""" 
TASK 
n this exercise you will create a program that displays a multiplication table that
shows the products of all combinations of integers from 1 times 1 up to and including
10 times 10. Your multiplication table should include a row of labels across the top
of it containing the numbers 1 through 10. It should also include labels down the left
side consisting of the numbers 1 through 10. The expected output from the program
is shown below:
1
2
3
4
5
6
7
8
9
10
1
1
2
3
4
5
6
7
8
9
10
2
2
4
6
8
10
12
14
16
18
20
3
3
6
9
12
15
18
21
24
27
30
4
4
8
12
16
20
24
28
32
36
40
5
5
10
15
20
25
30
35
40
45
50
6
6
12
18
24
30
36
42
48
54
60
7
7
14
21
28
35
42
49
56
63
70
8
8
16
24
32
40
48
56
64
72
80
9 10
9 10
18 20
27 30
36 40
45 50
54 60
63 70
72 80
81 90
90 100
When completing this exercise you will probably find it helpful to be able to
print out a value without moving down to the next line. This can be accomplished
by added end="" as the last argument to your print statement. For example,
print("A") will display the letter A and then move down to the next line. The
statement print("A", end="") will display the letter A without moving down
to the next line, causing the next print statement to display its result on the same line
as the letter A.
"""

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 10 

# main string 
print('    ', end='')
for i in range(MINIMUM_NUMBER, MAXIMUM_NUMBER + 1):
    print(f'{i:4}', end='')
print()

# multiplicate
for i in range(MINIMUM_NUMBER, MAXIMUM_NUMBER + 1):
    print(f'{i:4}', end='')
    for j in range(MINIMUM_NUMBER, MAXIMUM_NUMBER + 1):
        print(f'{i * j:4}', end='')
        
print()