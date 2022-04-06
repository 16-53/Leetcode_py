class Solution:
    def mySqrt(self, x: int) -> int:
        n = 1
        while n:
            s = n * n
            if s == x:
                return n
            elif s > x:
                return n - 1
            n += 1
