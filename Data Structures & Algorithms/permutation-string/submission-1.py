class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqMap = dict()
        for char in s1:
            if char in freqMap:
                freqMap[char] += 1
            else:
                freqMap[char] = 1
        winSize = len(s1)
        i = 0
        j = i + winSize - 1
        if j > len(s2):
            return False
        window = s2[i:j+1]
        freqMap2 = dict()
        for char in window:
            if char in freqMap2:
                freqMap2[char] += 1
            else:
                freqMap2[char] = 1
        if freqMap2 == freqMap:
            return True
        i += 1
        j += 1
        while j < len(s2):
            freqMap2[s2[i - 1]] -= 1
            if freqMap2[s2[i - 1]] == 0:
                freqMap2.pop(s2[i - 1], None)
            if s2[j] in freqMap2:
                freqMap2[s2[j]] += 1
            else:
                freqMap2[s2[j]] = 1
            if freqMap2 == freqMap:
                return True
            i += 1
            j += 1
        return freqMap2 == freqMap