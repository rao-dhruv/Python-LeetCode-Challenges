class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        pair=0
        for i in range(l):
            for j in range(l):
                if nums[i]==nums[j] and i<j:
                    pair=pair+1
        return pair
    nums=[1,2,3,1,1,3]
    print(numIdenticalPairs)