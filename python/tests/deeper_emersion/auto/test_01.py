#! /usr/bin/env python3 

import unittest

class MyTestCase(unittest.TestCase):
    def test_one(self):
        pass
    
    def not_a_test(self):
        pass
    
class MySecondTestCase(unittest.TestCase):
    
    def test_two(self):
        pass
    
    def test_two_part2(self):
        pass
    
if __name__ == '__main__':
    unittest.main()