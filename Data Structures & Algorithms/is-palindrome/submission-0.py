import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        formattedString = re.sub(r'[^a-z0-9]', '', s.lower())
        i = 0
        j = len(formattedString) - 1
        while i < j:
            if formattedString[i] != formattedString[j]:
                return False
            i += 1
            j -= 1
        return True