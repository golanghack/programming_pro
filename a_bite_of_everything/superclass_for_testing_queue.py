#! /usr/bin/env python3 


class QueueTests:
    """Super class for tests queue."""
    
    def testinit(self):
        queue = self.Queue()
        
    def test_add_and_remove_one_item_in_queue(self):
        queue = self.Queue()
        queue.enqueue(3)
        
        self.assertEqual(queue.dequeue(), 3)
        
    def test_alter_add_and_remove_from_queue(self):
        queue = self.Queue()
        for i in range(1000):
            queue.enqueue(i)
            
            self.assertEqual(queue.dequeue(), i)
            
    def test_many_operations(self):
        queue = self.Queue()
        for i in range(1000):
            queue.enqueue(2 * i + 3)
        for i in range(1000):
            self.assertEqual(queue.dequeue(), 2 * i + 3)
            
    def test_lenght(self):
        queue = self.Queue()
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
        
        
        
    