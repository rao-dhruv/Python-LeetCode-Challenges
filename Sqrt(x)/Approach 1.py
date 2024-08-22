class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        r = 1
        while r * r <= x:
            r += 1
        return r - 1