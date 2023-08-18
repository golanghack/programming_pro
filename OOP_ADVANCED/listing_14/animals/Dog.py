#! /usr/bin/env python3 

from Animal import Animal

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self, 'Cat')

    def make_sound(self):
        print('NOT WOW')