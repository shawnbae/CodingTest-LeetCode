import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp= [sr for sr in s.replace(" ","").lower() if sr not in string.punctuation]
        return tmp==tmp[::-1]