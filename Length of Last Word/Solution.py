class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        my_string = s.rstrip()
        counter=len(my_string)-1
        for i in range(counter,-1,-1):
            if s[i]==" ":
                return len(my_string)-(i+1)
                break
        return len(my_string)