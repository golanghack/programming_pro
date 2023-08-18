#! /usr/bin/env python3 

import unittest
from DayOfTheWeek import DayOfTheWeek

class TestDayOffTheWeek(unittest.TestCase):
    
    def testInitWithAbbreviation(self):
        my_day = DayOfTheWeek('Fri')
        self.assertEqual(my_day.name(), 'Friday')
        
        my_day = DayOfTheWeek('Sun')
        self.assertEqual(my_day.name(), 'Sunday')
        
if __name__ == '__main__':
    unittest.main()