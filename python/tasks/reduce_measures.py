#! /usr/bin/env python3 

"""  
TASK 

Many recipe books still use cups, tablespoons and teaspoons to describe the volumes
of ingredients used when cooking or baking. While such recipes are easy enough to
follow if you have the appropriate measuring cups and spoons, they can be difficult
to double, triple or quadruple when cooking Christmas dinner for the entire extended
family. For example, a recipe that calls for 4 tablespoons of an ingredient requires 16
tablespoons when quadrupled. However, 16 tablespoons would be better expressed
(and easier to measure) as 1 cup.
Write a function that expresses an imperial volume using the largest units pos-
sible. The function will take the number of units as its first parameter, and the unit
of measure (cup, tablespoon or teaspoon) as its second parameter. It will return a
string representing the measure using the largest possible units as its only result. For
example, if the function is provided with parameters representing 59 teaspoons then
it should return the string “1 cup, 3 tablespoons, 2 teaspoons”.
Hint: One cup is equivalent to 16 tablespoons. One tablespoon is equivalent
to 3 teaspoons.
"""

TEASSPOON = 1
SPOON = TEASSPOON * 3
CUP = SPOON * 16


def recipe_converters(unit: int, type_containts: str) -> str:
    """Return converted contains""" 
    
    tea_unit = unit // TEASSPOON
    sp_unit = tea_unit // 3
    c_unit = sp_unit // 16

    teaspoon_unit = str(tea_unit)
    spoon_unit = str(sp_unit)
    cup_unit = str(c_unit)

    complete_s = ''
    if teaspoon_unit or spoon_unit or cup_unit > 1:
        complete_s = '`s'
    
    full_string_teaspoon = f'Tea spoon -> {teaspoon_unit.join(complete_s)}'
    full_string_spoon = f'Spoon_unit -> {spoon_unit.join(complete_s)}'
    full_string_cup = f'cup_unit -> {cup_unit.join(complete_s)}'
    
    if type_containts == 'teaspoon':
        return full_string_teaspoon
    if type_containts == 'spoon':
        return full_string_spoon
    if type_containts == 'cup':
        return full_string_cup

def main():
    ingredients = 323
    my_type = 'spoon'

    result = recipe_converters(ingredients, my_type)
    if result == None:
        print('Error. Try again')
    
    else:
        print(result)
if __name__ == '__main__':
    main()