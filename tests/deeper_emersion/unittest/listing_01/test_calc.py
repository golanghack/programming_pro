#! /usr/bin/env python3 

import unittest
from Calc import Calc

class TestCalc(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calc()
        
    def test_add_method_returns_correct_result(self):
        self.assertEqual(6, self.calc.add(3, 3))
        
    def test_add_method_raises_typeerror_if_not_integers(self):
        self.assertRaises(TypeError, self.calc.add, 'A', 'B')
        
if __name__ == '__main__':
    unittest.main()