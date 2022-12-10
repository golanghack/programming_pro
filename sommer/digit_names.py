#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--DIGIT NAMES-->"""

import sys 

Language = "en"

ENGLISH = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
           5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
FRENCH = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4: "quatre",
          5: "cinq", 6: "six", 7: "sept", 8: "huit", 9: "neuf"}
RUSSIAN = {0: "ноль", 1: "один", 2: "два", 3: "три", 4: "четыре",
           5: "пять", 6: "цусть", 7: "семь", 8: "восемь", 9: "девять"}

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        print(f'usage --> {sys.argv[0]} [en|fr|ru] number')
        sys.exit()
    args = sys.argv[1:]
    if args[0] in {'en', 'fr', 'ru'}:
        global Language
        Language = args.pop(0)
    print_digits(args.pop(0), args.pop(1))
    
def print_digits(*digits):
    """print_digits function return reconstruction numbers from one lang to another lang."""
    
    dictonary = ENGLISH or FRENCH if Language == 'en' or 'fr' else RUSSIAN
   
    print(digits)
    for digit in digits:
        print(digit)
        #print(dictonary[int(digit, base=10)], end=' ')
    print()
    
    
if __name__ == '__main__':
    main()