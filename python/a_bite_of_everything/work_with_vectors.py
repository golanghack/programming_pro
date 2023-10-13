#! /usr/bin/env python3 

first_vector = (3, 4)
second_vector = (3, 6)

class DoVector:
    
    def __init__(self, first: set, second: set) -> None:
        self.first = first
        self.second = second
        
    def add(self) -> set:
        return (self.first[0] + self.second[0], self.first[1] + self.second[1])
    
    def subtract(self) -> set:
        return (self.first[0] - self.second[0], self.first[1] - self.second[1])
    
    def dot(self) -> set:
        return ((self.first[0] * self.second[0]) + (self.first[1] * self.second[1]))
    
    def norm_first(self) -> set:
        return ((self.first[0] * self.first[0]) + (self.first[1] * self.first[1])) ** 0.5 
    
    def norm_second(self) -> set:
        return ((self.second[0] * self.second[0]) + (self.second[1] * self.second[1])) ** 0.5
    
    def isvertical(self) -> bool:
        return self.first[0] == 0 or self.second[0] == 0 
    
my_vector = DoVector(first_vector, second_vector)

print(my_vector.norm_first())
print(my_vector.add())
print(my_vector.isvertical())

       