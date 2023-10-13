#! /usr/bin/env python3 

from BufferedIterator import BufferedIterator

def merge_iterators(iterator_one, iterator_two):
    iter_one = BufferedIterator(iterator_one)
    iter_two = BufferedIterator(iterator_two)
    
    while iter_one.hash_next() or iter_two.hash_next():
        if not iter_one.hash_next() or (iter_two.hash_next() and iter_two.peek() < iter_one.peek()):
            yield next(iter_two)
        else:
            yield next(iter_one)
    