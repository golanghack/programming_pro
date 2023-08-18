#! /usr/bin/env python3


class Animal: 

    def __init__(self, species):
        self.__species = species

    def show_species(self):
        print('I am -> ', self.__species)

    def make_sound(self):
        print('WOW')

""" 
>>> import Animal
>>> common_animal = Animal.Animal('Usualy')
>>> common_animal.show_species()
'Usualy'
>>> common_animal.make_sound()
'WOW'
"""
    
if __name__ == '__main__':
    
    import doctest
    doctest.testmod()