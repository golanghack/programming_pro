#! /usr/bin/env python3 

import unittest
from add.addition import addition

class AdditionTestCase(unittest.TestCase):
    
    def test_main(self):
        result = addition(3, 2)
        assert result == 5
        
if __name__ == '__main__':
    unittest.main()
        