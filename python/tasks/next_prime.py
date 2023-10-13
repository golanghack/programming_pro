#! /usr/bin/env python3 

""" 
TASK 

In this exercise you will create a function named nextPrime that finds and returns
the first prime number larger than some integer, n. The value of n will be passed to
the function as its only parameter. Include a main program that reads an integer from
the user and displays the first prime number larger than the entered value.
""" 

from util_for_tasks.get_number import get_number

def is_prime(number: int) -> bool:
    """Return boolean for input number
    
    >>> number = 11
    >>> is_prime(number)
    True
    >>> number = 12
    >>> is_prime(number)
    False
    """
    if number == 1:
        return True
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                return False
        return True
    return False


def list_prime_formation(number):
    """Return list of simple numbers.
    
    >>> number = 1
    >>> list_prime_formation(number)
    [3]
    """

    list_primes = []
    if number != 0:
        mutation = number + 2
        if is_prime(mutation):
            list_primes.append(mutation)
        return list_primes

def result():
    print('Enter number from 0 to 112.')
    number = get_number('Enter number -> ')
    primes_list = list_prime_formation(number)
    print(f'Next prime number -> {primes_list[0]}')

def main():
    try:
        result()
    except TypeError as err:
        print(f'You entered zero number and error -> {err}')
        print('Number must be from 1 non zero')
        print('Try again. One time.')
        result()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
