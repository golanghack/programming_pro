#! /usr/bin/env python3 

from typing import Any

class Doubler:
    """Simple class for doubles means.
    example input 2 output -> 4
    """
    
    def __init__(self, n: Any) -> None:
        self._n = 2 * n 
        
    def comeback_n(self) -> Any:
        return self._n
    
def test_doubler() -> None:
    x = Doubler(5)
    y = Doubler(-4)
    z = Doubler('d')
    
    assert(x.comeback_n() == 10)
    assert(y.comeback_n() == -8)
    assert(z.comeback_n() == 'dd')