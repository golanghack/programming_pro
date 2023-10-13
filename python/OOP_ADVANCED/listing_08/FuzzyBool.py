#! /usr/bin/env python3 

""" 
Implements an immutable FuzzyBool data type that can only have
values inthe interval [0.0, 1.0] and which supports the basic logical
operations 
not (~), and (&), and or (|) using Fuzzy logic.

>>> f = FuzzyBool()
>>> g = FuzzyBool(.5)
>>> h = FuzzyBool(3.75)
>>> f, g, h 
(FuzzyBool(0.0), FuzzyBool(0.5), FuzzyBool(0.0))
>>> h = ~h 
>>> print(f, g, h)
0.0 0.5 1.0
""" 

import Util

@Util.complete_comparisons
class FuzzyBool:

    def __init__(self, value: float=0.0) -> None:
        """ 
        >>> f = FuzzyBool()
        >>> g = FuzzyBool(.5)
        >>> h = FuzzyBool(3.75)
        >>> f, g, h
        (FuzzyBool(0.0), FuzzyBool(0.5), FuzzyBool(0.0))
        """

        self.__value = value if 0.0 <= value <= 1.0 else 0.0 

    def __invert__(self):
        """Returns the logical not of this FuzzyBool

        >>> f = FuzzyBool(.125)
        >>> ~f
        FuzzyBool(0.875)
        >>> ~FuzzyBool()
        FuzzyBool(1.0)
        >>> ~FuzzyBool(1)
        FuzzyBool(0.0)
        """ 

        return FuzzyBool(1.0 - self.__value)

    def __and__(self, other):
        """Returns the logical and of this FuzzyBool and the other one 

        >>> FuzzyBool(.5) & FuzzyBool(.6)
        FuzzyBool(0.5)
        """ 

        return FuzzyBool(min(self.__value, other.__value))


    def __iand__(self, other):
        """Applies logical and to this FuzzyBool with the other one

        >>> f = FuzzyBool(.5)
        >>> f &= FuzzyBool(.6)
        >>> f 
        FuzzyBool(0.5)
        """ 

        self.__value = min(self.__value, other.__value)
        return self

    @staticmethod
    def conjuction(*fuzzies):
        """Returns the logical and of all the FuzzyBools

        >>> FuzzyBool.conjuction(FuzzyBool(.5), FuzzyBool(.6), .2, .125)
        FuzzyBool(0.125)
        """ 

        return FuzzyBool(min([float(x) for x in fuzzies]))

    def __or__(self, other):
        """Returns the logical or of this FuzzyBool and the other one 

        >>> FuzzyBool(.5) | FuzzyBool(.75)
        FuzzyBool(0.75)
        """ 

        return FuzzyBool(max(self.__value, other.__value))


    def __ior__(self, other):
        """Applies logical or to this FuzzyBool with the other one 

        >>> f = FuzzyBool(.5)
        >>> f |= FuzzyBool(.75)
        >>> f 
        FuzzyBool(0.75)
        """ 

        self.__value = max(self.__value, other.__value)
        return self 

    @staticmethod
    def disjunction(*fuzzies):
        """Returns the logical or of all the FuzzyBools

        >>> FuzzyBool.disjunction(FuzzyBool(.5), FuzzyBool(.75), .2, .1)
        FuzzyBool(0.75)
        """ 

        return FuzzyBool(max([float(x) for x in fuzzies]))


    def __repr__(self):
        """ 

        >>> f = FuzzyBool(.5)
        >>> repr(f)
        'FuzzyBool(0.5)'
        """ 

        return (f'{self.__class__.__name__}({self.__value})')

    def __str__(self):
        """ 

        >>> f = FuzzyBool(.5)
        >>> str(f)
        '0.5'
        """ 

        return str(self.__value)

    
    def __bool__(self):
        """ 

        >>> f = FuzzyBool(.3)
        >>> g = FuzzyBool(.51)
        >>> bool(f), bool(g)
        (False, True)
        """ 

        return self.__value > 0.5 

    
    def __int__(self):
        return round(self.__value)

    def __float__(self):
        return self.__value 

    def __lt__(self, other):
        return self.__value < other.__value

    def __eq__(self, other):
        return self.__value == other.__value

    def __hash__(self):
        return hash(id(self))

    def __format__(self, format_spec):
        """ 
        
        >>> f = FuzzyBool(.875)
        >>> "{0:.0%}".format(f)
        '88%'
        >>> "{0:.1%}".format(f)
        '87.5%'
        """ 

        return format(self.__value, format_spec)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    