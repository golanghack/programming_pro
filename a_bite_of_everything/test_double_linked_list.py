#! /usr/bin/env python3

from DoubleLinkedList import DoubleLinkedList

def test_doble_linked_list():
    
    a = DoubleLinkedList()
    [a.add_last(i) for i in range(11)]

    b = DoubleLinkedList()
    [b.add_last(i + 11) for i in range(10)]
    
    a += b
    n = a._head
    while n is not None:
        print(n.data, end=' ')
        n = n.link 
    
    assert(test_doble_linked_list() == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20')
        

        
        

