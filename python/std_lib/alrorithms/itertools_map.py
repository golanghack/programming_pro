#! /usr/bin/env python3

def times_two(x: int) -> int:
    return 2 * x 

def multiply(x: int, y: int) -> int:
    return (x, y, x * y)

print('Doubles -> ')

for i in map(times_two, range(5)):
    print(i)
    
print('\nMultiplyes -> ')

r1 = range(5)
r2 = range(3)
for i in map(multiply, r1, r2):
    print('{:d} * {:d} = {:d}'.format(*i))
    
print('nStopping -> ')
r1 = range(5)
r2 = range(2)
for i in map(multiply, r1, r2):
    print(i)