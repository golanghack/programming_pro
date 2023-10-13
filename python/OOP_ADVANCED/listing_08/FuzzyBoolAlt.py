#! /usr/bin/env python3 

""" 
Implements an immutable FuzzyBool data that can only have values 
in the interval [0.0, 1.0] and swithc supports the basic logical 
operations not (~), and (&), or (|) using fuzzy logic.

Tests 
>>> f = FuzzyBool()
>>> g = FuzzyBool(.5)
>>> h = FuzzyBool(3.75)
>>> print(f, g, h)
0.0 0.5 0.0
>>> h = ~h 
>>> f = FuzzyBool(.2)
>>> f < g 
True
>>> f + g 
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +: 'FuzzyBool' and 'FuzzyBool'
>>> -f 
Traceback (most recent call last):
... 
TypeError: bad operand type for unary -: 'FuzzyBool'
>>> int(h), int(g), int(FuzzyBool(.51))
(1, 0, 1)
>>> f = FuzzyBool(.5)
>>> str(f)
'0.5'
""" 

def conjunction(*fuzzies):
    """Returns the logacal and of all the FuzzyBools

    >>> conjunction(FuzzyBool(.5), FuzzyBool(.6), .2, .125)
    FuzzyBool(0.125)
    """ 

    return FuzzyBool(min(fuzzies))


def disjunction(*fuzzies):
    """Returns the logical or of all the FuzzyBoools

    >>> disjunction(FuzzyBool(.5), FuzzyBool(.75), .2, .1)
    FuzzyBool(0.75)
    """ 

    return FuzzyBool(max(fuzzies))


class FuzzyBool(float):

    def __new__(cls, value: float=0.0):
        """ 
        >>> f = FuzzyBool()
        >>> g = FuzzyBool(.5)
        >>> h = FuzzyBool(3.75)
        >>> f, g, h
        (FuzzyBool(0.0), FuzzyBool(0.5), FuzzyBool(0.0.))
        """ 

        return super().__new__(cls, value if 0.0 <= value <= 1.0 else 0.0)

    
    def __invert__(self):
        """Return the logical not of thsi FuzzyBool

        >>> f = FuzzyBool(.125)
        >>> ~f 
        FuzzyBool(0.875)
        >>> ~FuzzyBool()
        FuzzyBool(1.0)
        >>> ~FuzzyBool(1)
        FuzzyBool(0.0)
        """ 

        return FuzzyBool(1.0 - float(self))


    def __and__(self, other):
        """Returns the logical and of this FuzzyBool and the other one 

        >>> FuzzzyBool(.5) & FuzzyBool(.6)
        FuzzyBool(0.5)
        """ 

        return FuzzyBool(min(self, other))

    
    def __iand__(self, other):
        """Applies logical and to this FuzzyBool with the ither one 

        >>> f = FuzzyBool(.5)
        >>> f &= FuzzyBool(.6)
        >>> f 
        FuzzyBool(0.5)
        """ 

        return FuzzyBool(min(self, other))


    def __or__(self, other):
        """Returns the logical or of this FuzzyBool and the other one 

        >>> FuzzyBool(.5) | FuzzyBool(.75)
        FuzzyBool(0.75)
        """ 

        return FuzzyBool(max(self, other))


    def __ior__(self, other):
        """Applies logical or to this FuzzyBool with the other one 

        >>> f = FuzzyBool(.5)
        >>> f |= FuzzyBool(.75)
        >>> f
        FuzzyBool(0.75)
        """ 

        return FuzzyBool(max(self, other))


    def __repr__(self):
        """ 
        >>> f = FuzzyBool(.5)
        >>> repr(f)
        'FuzzyBool(0.5)'
        """ 

        return (f'{self.__class__.__name__}({super().__repr__()})')


    def __bool__(self):
        """ 
        >>> f = FuzzyBool(.3)
        >>> g = FuzzyBool(.51)
        >>> bool(f), bool(g)
        (False, True)
        """ 

        return self > 0.5 

    
    def __int__(self):
        """ 
        >>> f = FuzzyBool(.3)
        >>> g = FuzzyBool(.51)
        >>> int(f), int(g)
        (0, 1)
        """ 

        return round(self)


    for name, operator in (('__neg__', '-'), 
                            ('__index__', 'index()')):
                            message = ("bad operand type for unary {0}: '{{self}}'".format(operator))
                            exec("def {0}(self): raise TypeError(\"{1}\".format("
             "self=self.__class__.__name__))".format(name, message))

    for name, operator in (('__xor__', '^'), 
                    ('__ixor__', '^='),
                    ("__add__", "+"), ("__iadd__", "+="), ("__radd__", "+"),
            ("__sub__", "-"), ("__isub__", "-="), ("__rsub__", "-"),
            ("__mul__", "*"), ("__imul__", "*="), ("__rmul__", "*"),
            ("__pow__", "**"), ("__ipow__", "**="),
            ("__rpow__", "**"), ("__floordiv__", "//"),
            ("__ifloordiv__", "//="), ("__rfloordiv__", "//"),
            ("__truediv__", "/"), ("__itruediv__", "/="),
            ("__rtruediv__", "/"), ("__divmod__", "divmod()"),
            ("__rdivmod__", "divmod()"), ("__mod__", "%"),
            ("__imod__", "%="), ("__rmod__", "%"),
            ("__lshift__", "<<"), ("__ilshift__", "<<="),
            ("__rlshift__", "<<"), ("__rshift__", ">>"),
            ("__irshift__", ">>="), ("__rrshift__", ">>")):
            message = ('unsupported operand type(s) for {0} -> '
            '"{{self}}"{{join}} {{args}}'.format(operator))

            exec("def {0}(self, *args):\n"
             "    types = [\"'\" + arg.__class__.__name__ + \"'\" "
             "for arg in args]\n"
             "    raise TypeError(\"{1}\".format("
             "self=self.__class__.__name__, "
             "join=(\" and\" if len(args) == 1 else \",\"),"
             "args=\", \".join(types)))".format(name, message))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
