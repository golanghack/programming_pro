#! /usr/bin/env python3 

""" 
Рассмотрим задачу вывода на экран цифр некото-
рого неотрицательного целого числа n вертикально в прямом поряд-
ке
345
3
4
5
"""

def vertically_numbers(n: int) -> str:
    """Return vertical numbers."""
    
    if n < 10:
        print(n)
    else:
        print(n // 10)
        vertically_numbers(n % 10)
        
