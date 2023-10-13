#! /usr/bin/env python3 

from Progression import Progression

class GeometricProgression(Progression):
    """Iterator producin a geometric progression""" 

    def __init__(self, base: int=2, start: int=1):
        """Create a new geometric progression.

        base    -> the fixed constants multipied to easch term(default 2)
        start   -> the first term of the progression(default 1)
        """ 

        super().__init__(start)
        self._base = base

    def _advance(self):
        """Update current value by multiplying it by the base value""" 

        self._current *= self._base
        