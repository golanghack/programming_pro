#! /usr/bin/env python3 

class Vector:
    """Represent a vector in a multidimensional space""" 

    def __init__(self, d: int) -> None:
        """Create d-dimensional vector of zeros"""

        self.__coords = [0] * d 

    def __len__(self) -> int:
        """Return the dimension or the vector"""

        return len(self.__coords)

    def __getitem__(self, j):
        """return jth coordinate of vector""" 

        return self.__coords[j]

    def __setitem__(self, j, value):
        """Set jth coordinate of vector to given value""" 

        self.__coords[j] = value

    def __add__(self, other):
        """Return sum of two vectors""" 

        if len(self) != len(other):
            raise ValueError('dimensions myust agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""

        return self.__coords == other.__coords

    def __ne__(self, other):
        """Return True if vector differs from other""" 

        return not self == other

    def __str__(self):
        """Produce string represention of vector""" 

        return '<' + str(self.__coords)[1:-1] + '>'

if __name__ == '__main__':
    v = Vector(6)
    v[1] = 1
    v[-1] = 6
    print(v)
    u = v + v
    print(u)

    total = 0
    for entry in v:
        total += entry
    print(total)