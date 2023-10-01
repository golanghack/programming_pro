#! /usr/bin/env python3 

import unittest
from LinkedQueue import LinkedQueue

class TestListQueue(unittest.TestCase):
    
    def testinit(self):
        queue = LinkedQueue()
    
    def test_add_and_remove_one_item(self):
        queue = LinkedQueue()
        queue.enqueue(3)
        
        self.assertEqual(queue.dequeue(), 3)
        
    def test_alter_add_remove(self):
        queue = LinkedQueue()
        for i in range(1000):
            queue.enqueue(i)
            
            self.assertEqual(queue.dequeue(), i)
    def test_mny_operations(self):
        queue = LinkedQueue()
        
        for i in range(1000):
            queue.enqueue(2 * i + 3)
            
        for i in range(1000):
            self.assertEqual(queue.dequeue(), 2 * i + 3)
            
    def test_lenght(self):
        queue = LinkedQueue()
        
        self.assertEqual(len(queue), 0)
        
        for i in range(10):
            queue.enqueue(i)
        self.assertEqual(len(queue), 10)
        
        for i in range(10):
            queue.enqueue(i)
        self.assertEqual(len(queue), 20)
        
        for i in range(15):
            queue.dequeue()
        self.assertEqual(len(queue), 5)
        
if __name__ == '__main__':
    unittest.main()

