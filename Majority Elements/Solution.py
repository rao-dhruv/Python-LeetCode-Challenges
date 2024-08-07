class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = len(nums)
        for i in nums:
            if nums.count(i)>(a/2):
                return i