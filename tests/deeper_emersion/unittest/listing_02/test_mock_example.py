#! /usr/bin/env python3 

import unittest
from mock import Mock

class Test_Mocking(unittest.TestCase):
    """Test mocking with mock library."""
    
    def test_mock_method_returns(self):
        """Testing Mock"""
        
        my_mock = Mock()
        my_mock.my_method.return_value = 'hello'
        self.assertEqual('hello', my_mock.my_method())
        
if __name__ == '__main__':
    unittest.main()