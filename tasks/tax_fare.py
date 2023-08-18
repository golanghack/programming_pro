#! /usr/bin/env python3 

""" 
TASK 

In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25
for every 140 meters travelled. Write a function that takes the distance travelled (in
kilometers) as its only parameter and returns the total fare as its only result. Write a
main program that demonstrates the function.
Hint: Taxi fares change over time. Use constants to represent the base fare and
the variable portion of the fare so that the program can be updated easily when
the rates increase.
"""

from util_for_tasks.get_number import get_number

BASE_RATE: float = 4.00
DIFFERENT_RATE: float = 0.25
BASE_DISTANCE_RATE: float = 0.14
MESSAGE: str = 'Enter distance for taxi in km -> '

def main():
    distance: int = get_number(MESSAGE)
    result = 0
    if distance > BASE_DISTANCE_RATE:
        result = (BASE_RATE + (distance / BASE_DISTANCE_RATE) * DIFFERENT_RATE)
    else:
        result = BASE_RATE

    print(f'Tax Fare for distance -> {distance} km -> {result:.2f}$')


if __name__ == '__main__':
    main()


