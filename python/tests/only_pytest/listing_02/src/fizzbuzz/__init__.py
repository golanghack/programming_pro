#! /usr/bin/env python3 

def is_fizz(n: int) -> bool:
    return n % 3 == 0

def is_buzz(n: int) -> bool:
    return n % 5 == 0

def out_fizz():
    print('fizz', end='')

def out_buzz():
    print('buzz', end='')

def end_num(n):
    if is_fizz(n) or is_buzz(n):
        n = ''
    print(n)

def fizzbuzz(numbers):
    for number in numbers:
        if is_fizz(number):
            out_fizz()
        if is_buzz(number):
            out_buzz()
        end_num(number)

def main():
    fizzbuzz(range(100))

if __name__ == '__main__':
    main()