class Solution:
    def isValid(self, word: str) -> bool:
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        vowels = "aeiouAEIOU"
        
        has_vowel = any(char in vowels for char in word)
        has_consonant = any(char in consonants for char in word)
        
        return len(word) >= 3 and has_vowel and has_consonant