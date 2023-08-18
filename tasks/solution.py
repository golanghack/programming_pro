#! /usr/bin/env python3 

from functools import lru_cache


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        @lru_cache(None)
        def f(s, c, m):
            if s == 0:
                return c % 2 == m % 2
            if c == m:
                return 0

            h = [f(s - i ** 2, c + 1, m) for i in range(1, int(s ** 0.5) + 1)]

            return any(h) if c % 2 != m % 2 else all(h)


        if any(f(n, 0 ,m) for m in range(1, int(n ** 0.5) + 5, 2)):
            return True
        
        return False

d = Solution()
c = d.winnerSquareGame(4)
print(c)