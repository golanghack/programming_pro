#! /usr/bin/env python3 

from cards import Card

class TestEquality:
    """Testing equality all functions in tests"""
    
    def test_equality(self):
        c1 = Card('something', 'brian', 'todo', 123)
        c2 = Card('something', 'brian', 'todo', 123)
        assert c1 == c2 
        
    def test_equality_with_diff_ids(self):
        c1 = Card('something', 'brian', 'todo', 123)
        c2 = Card('something', 'brian', 'todo', 4566)
        assert c1 == c2 
        
    def test_inequality(self):
        c1 = Card('something', 'brian', 'todo', 123)
        c2 = Card('completely different', 'okken', 'done', 123)
        assert c1 != c2 
        
    
    
    