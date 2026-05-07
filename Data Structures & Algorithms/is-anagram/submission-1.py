class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_table1 = {}
        freq_table2 = {}
        for char in s:
            if char in freq_table1:
                num = freq_table1[char]
                num += 1
                freq_table1[char] = num
            else:
                freq_table1[char] = 1
        for char in t:
            if char in freq_table2:
                num = freq_table2[char]
                num += 1
                freq_table2[char] = num
            else:
                freq_table2[char] = 1
        if freq_table1 == freq_table2:
            return True
        else:
            return False