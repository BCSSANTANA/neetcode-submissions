class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        seen = dict()
        i = -1
        for char in s:
            i += 1
            if char in seen:
                maxLength = max(maxLength, len(seen))
                start = seen[char] + 1
                seen.clear()
                for otherChar in s[start:i]:
                    seen[otherChar] = start
                    start += 1
                seen[char] = i
            else:
                seen[char] = i
        return max(maxLength, len(seen))
        