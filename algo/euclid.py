#! /usr/bin/env python3

"""EUCLID"""

def euclid(x, y):
    larger = max(x, y) 
    smaller = min(x, y)
        
    remainder = larger % smaller
    
    if (remainder == 0):
        return smaller
    else:
        return euclid(smaller, remainder) 
    
    
    
    

print(euclid(12, 1))