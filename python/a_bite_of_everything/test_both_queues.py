#! /usr/bin/env python3 

import unittest
from superclass_for_testing_queue import QueueTests
from ListQueueFakeDelete import ListQueueFakeDelete
from LinkedQueue import LinkedQueue


def _test(queue_class: str):
    class QueueTestCase(unittest.TestCase, QueueTests):
        Queue = queue_class
    return QueueTestCase


TestLinkedQueue = _test(LinkedQueue)
TestListQueue = _test(ListQueueFakeDelete)

if __name__ == '__main__':
    unittest.main()