#! /usr/bin/env python3 

import unittest
from add.addition import addition, sub_addition

class AdditionTestCase(unittest.TestCase):
    
    def test_main_addition(self):
        result = addition(3, 2)
        assert result == 5
        
    def test_main_sub_addition(self):
        result = sub_addition(3, 2)
        assert result == 5
        
if __name__ == '__main__':
    unittest.main()
        