#! /usr/bin/env python3

import unittest
from fibonachi import fib

class Test(unittest.TestCase):
    
    def test_fibo(self):
        result = fib(7)
        self.assertEqual(result, 13)
        
if __name__ == '__main__':
    unittest.main()