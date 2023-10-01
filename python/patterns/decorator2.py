#! /usr/bin/env python3 

"""<--DECORATOR-->"""

import numbers

def ensure(name: str, validate, doc: str=None):
    """create decorator of class"""
    
    def decorator(Class):
        """create private attr of class"""
        
        private_name = '__', + name
        
        def getter(self):
            """return mean of attribute"""
            
            return getattr(self, private_name)
        
        def setter(self, value):
            """call validation function and set  write new mean"""
            
            validate(name, value)
            setattr(self, private_name, value)
        #create attribute or write in attribute
        setattr(Class, name, property(getter, setter, doc=doc))
        return Class
    return decorator

def is_non_empty_str(name: str, value: str):
    """Testing empty string or str type"""
    
    if not isinstance(value, str):
        raise ValueError(f'{name} must be of type str')
    if not bool(value):
        raise ValueError(f'{name} may not be empty')
    
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

def is_valid_isbn(isbn):
    """testing lenght of isbn number"""
    
    if len(isbn) != 10:
        raise ValueError(f'{isbn} must by lenght 10')
    return isbn



@ensure('title', is_non_empty_str)
@ensure('isbn', is_valid_isbn)
@ensure('price', is_in_range(1, 10000))
@ensure('quantity', is_in_range(0, 10000000))
class Book:
    
    def __init__(self, title: str, isbn: int, price: float, quantity: int) -> None:
        self.title = title
        self.isbn = isbn
        self.price = price
        self.quantity = quantity
        
    @property
    def value(self):
        return self.price * self.quantity
    
    

