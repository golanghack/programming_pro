#! /usr/bin/env python3 

def foo(arr1, arr2):
    zone = []
    zone2=[]
    for i1, a1 in enumerate(arr1):
        for i2, a2 in enumerate(arr2):
            if a2 - a1<0:
                zone.append(i1)
                zone2.append(i2)
                break

    yield zone
    yield zone2

x1 = [1.11, 1.11, 1.12, 1.12, 1.13, 1.08, 1.65, 1.65, 1.05, 1.05, 1.05, 1.05, 1.1, 1.1, 1.05] 
x2 = [1.66, 1.66, 1.58, 1.58, 1.61, 1.61, 1.82, 1.82, 1.65, 1.65, 1.77, 1.77, 1.65, 1.65, 1.46] 
z1, z2 = foo(x1, x2)
print(z1, z2)

