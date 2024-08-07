class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = s.lower()
        bing=[]
        for i in pal:
            if i.isalnum():
                bing.append(i)
            else:
                continue
        
        for i in range(len(s)):
            if bing[::-1] == bing:
                return True
            else:
                return False

        