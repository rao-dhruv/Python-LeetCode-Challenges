class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(t)):
                if t[i] not in s or s.count(t[i])!=t.count(t[i]):
                    return False
            return True