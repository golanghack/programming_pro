#! /usr/bin/env python3 

# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""<--ELEMENTARY DECOATOR--POSITIVE RESULT-->"""

def positive_result(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        assert result >= 0, function.__name__ + '() result isn`t >= 0'
        return result
    wrapper.__name__ = function.__name__
    wrapper.__doc__ = function.__doc__
    return wrapper

@positive_result
def discriminant(a: int, b: int, c: int) -> int:
    return (b ** 2) - (2 * a * c)

if __name__ == '__main__':
    import pprint
    try:
        pprint.pprint(discriminant(1, 4, 1))
    except ValueError as err:
        print(f'Error -> {err} enter new integers')