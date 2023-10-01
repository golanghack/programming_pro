#! /usr/bin/env python3

from Progression import Progression

class ArithmeticProgression(Progression):
    """Iterator producin an arithmetic progression""" 

    def __init__(self, increment=1, start=0):
        """Create a ne arithmetic progression.

        increment -> the fixed contant to add(default 1)
        start     -> the first term of the progression(default 0)
        """ 

        super().__init__(start)
        self._increment = increment

    def _advance(self):
        """Update current value by adding the fixed increment""" 

        self._current += self._increment

        
