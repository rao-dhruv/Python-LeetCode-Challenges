class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
            s = ""
            s = s.join([str(i) for i in digits])
            s = int(s) + 1
            s = str(s)
            s = [int(i) for i in s]
            return s