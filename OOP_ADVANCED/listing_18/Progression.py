#! /usr/bin/env python3


class Progression:
    """Iterator -> progression.

    Default iterator -> 0, 1, 2, 3...
    """ 

    def __init__(self, start: int=0) -> None:
        """Initializing current the first value of the prog-n"""

        self._current = start

    def _advance(self):
        """Update self._current to a new value 

        This should be overriden by a subclass to customize progre-n

        By conbverction, if current is set to None, this desibnates the end
        of a finite progres-n
        """ 

        self._current += 1

    def __next__(self):
        """Return thwe next element or raise StopIteration"""

        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n: int):
        """Print next n values of the progression""" 

        print(' '.join(str(next(self)) for j in range(n)))