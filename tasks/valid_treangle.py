#! /usr/bin/env python3 

"""TASK 

If you have 3 straws, possibly of differing lengths, it may or may not be possible
to lay them down so that they form a triangle when their ends are touching. For
example, if all of the straws have a length of 6 inches then one can easily construct
an equilateral triangle using them. However, if one straw is 6 inches long, while
the other two are each only 2 inches long, then a triangle cannot be formed. More
generally, if any one length is greater than or equal to the sum of the other two then
the lengths cannot be used to form a triangle. Otherwise they can form a triangle.
Write a function that determines whether or not three lengths can form a triangle.
The function will take 3 parameters and return a Boolean result. If any of the lengths
are less than or equal to 0 then your function should return False. Otherwise it
should determine whether or not the lengths can be used to form a triangle using
the method described in the previous paragraph, and return the appropriate result.
In addition, write a program that reads 3 lengths from the user and demonstrates the
behaviour of your function.
"""

from util_for_tasks.get_number import get_number

def is_valid() -> bool:
    """Return boolean for valid treangle."""

    message = 'Enter nlenght of treangle side -> '
    side_a = get_number(message)
    side_b = get_number(message)
    side_c = get_number(message)

    if ((side_a >= (side_b + side_c))or 
                  (side_b >= (side_a + side_c)) or
                  (side_c >= (side_a + side_b)) and 
                  side_a == 0 or side_b == 0 or side_c == 0):
                  return False
    return True

def main():
    print(is_valid())

if __name__ == '__main__':
    main()