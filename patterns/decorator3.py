#! /usr/bin/env python3 

"""<--DECORATOR-->"""

def do_ensure(Class):
    def make_property(name, attribute):
        private_name = '__' + name
        
        def getter(self):
            return getattr(self, private_name)
        def setter(self, value):
            attribute.validate(name, value)
            setattr(self, private_name, value)
        return property(getter, setter, doc=attribute.doc)
    for name, attribute in Class.__dict__.items():
        if isinstance(attribute, Ensure):
            setattr(Class, name, make_property(name, attribute))
    return Class

def is_non_empty_str(name: str, value: str):
    """Testing empty string or str type"""
    
    if not isinstance(value, str):
        raise ValueError(f'{name} must be of type str')
    if not bool(value):
        raise ValueError(f'{name} may not be empty')

def is_valid_isbn(isbn):
    """testing lenght of isbn number"""
    
    if len(isbn) != 10:
        raise ValueError(f'{isbn} must by lenght 10')
    return isbn

class Ensure:
    def __init__(self, validate, doc=None):
        self.validate = validate
        self.doc = doc

def is_in_range(minimum: int=None, maximum: int=None):
    """Testing range for input date"""
    
    assert minimum is not None or maximum is not None
    def is_in_range(name, value):
        if not isinstance(value, numbers.Number):
            raise ValueError(f'{name} musr be a number')
        if minimum is not None and value < minimum:
            raise ValueError(f'{name} {value} is too small')
        if maximum is not None and value > maximum:
            raise ValueError(f'{name} {value} is too big')
    return is_in_range
      
@do_ensure
class Book:
    
    title = Ensure(is_non_empty_str)
    isbn = Ensure(is_valid_isbn)
    price = Ensure(is_in_range(1, 10000))
    quantity = Ensure(is_in_range(0, 10000000))
    
    def __init__(self, title, isbn, price, quantity):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.quantity = quantity
        
    @property
    def value(self):
        return self.price * self.quantity
    
    