class Solution:
    def isValid(self, word: str) -> bool:
        consonent = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        vowel = "aeiouAEIOU"
        if len(word)<3:
            return False
        elif(word.isalnum()==False):
            return False
        elif not any(char in vowel for char in word) or not any(char in consonent for char in word):
            return False
        else:
            return True