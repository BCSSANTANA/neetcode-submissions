class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for s in strs:
            sorted_s = sorted(s)
            sorted_string = ''.join(sorted_s)
            if sorted_string in d:
                d[sorted_string].append(s)
            else:
                d[sorted_string] = [s]
        return list(d.values())

        