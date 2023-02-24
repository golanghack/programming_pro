#! /usr/bin/env python3 

import unittest
from superclass_for_testing_queue import QueueTests
from LinkedQueue import LinkedQueue

class TestLinkedQueue(unittest.TestCase, QueueTests):
    Queue = LinkedQueue
    
if __name__ == '__main__':
    unittest.main()