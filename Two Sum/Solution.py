class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        watch={}
        i=0
        while i<len(nums):
            num=nums[i]
            find=target-num
            if find in watch:
                return [i,watch[find]]
            watch[num]=i
            i+=1