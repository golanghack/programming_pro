#! /usr/bin/env python3 

"""  
Problem 

You want to eliminate the duplicate values in a sequence, but preserve the order of the
remaining items.
""" 

# with hash
def delete_duplicates_hash(items):
    """  
    >>> a = [1, 5, 2, 1, 9, 1, 5, 10]
    >>> list(delete_duplicates_hash(a))
    [1, 5, 2, 9, 10]
    """ 
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

# no hash 
def delete_duplicates_no_hash(items, key=None):
    """  
    >>> a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 4, 'y': 4}]
    >>> list(delete_duplicates_no_hash(a, key=lambda d: (d['x'], d['y'])))
    [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
    """ 

    seen = set()
    for item in items:
        value = item if key is None else key(item)
        if value not in seen:
            yield item
            seen.add(value)

if __name__ == '__main__':
    import doctest
    doctest.testmod()