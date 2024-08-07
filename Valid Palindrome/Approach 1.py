class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = s.lower()
        bing=[]
        for i in pal:
            if i in "abcdefghijklmnopqrstuvwxyz0123456789":
                bing.append(i)
            else:
                continue
        
        if bing[::-1] == bing:
            return True
        else:
            return False