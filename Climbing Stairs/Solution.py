class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        climb = [0] * (n+1)
        climb[0] = climb[1] = 1
        for i in range(2, n+1):
            climb[i] = climb[i-1] + climb[i-2]
        return climb[n]
