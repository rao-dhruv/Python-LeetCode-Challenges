class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            desire = haystack.index(needle)
            return desire