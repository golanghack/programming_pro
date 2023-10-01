#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.


"""<--SIMPLE DECORATOR-->"""

from functools import wraps


#first decorator
def positive_result(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        assert result >= 0, function.__name__ + '() result isn`t >= 0'
        return result
    return wrapper

#second 
def bounded(minimum: int, maximum: int):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            if result < minimum:
                return minimum
            if result > maximum:
                return maximum
            return result
        return wrapper
    return decorator

@bounded(0, 100)
def percent(amount, total):
    return (amount / total) * 1000

if __name__ == '__main__':
    print(percent(12, 34))