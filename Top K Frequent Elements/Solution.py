class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        for i in nums:
            if i in mydict:
                mydict[i]+=1
            else:
                mydict[i]=1
        sorted_dict = list(dict(sorted(mydict.items(),key=lambda x:x[1], reverse=True)))
    return sorted_dict[:k]