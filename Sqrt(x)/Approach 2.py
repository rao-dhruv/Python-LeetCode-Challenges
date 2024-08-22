class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        else:
            start = 1
            end = x
            while start<=end:
                mid = (start + end)//2
                if mid == x//mid:
                    return mid
                elif mid>x//mid:
                    end = mid - 1
                else:
                    start = mid + 1
            return end