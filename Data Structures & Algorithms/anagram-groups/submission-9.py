class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pos = 0
        seen = set()
        seen_to_idx = {}
        anagram_l_list = []
        for elem in strs:
            freq_map = {}
            for char in elem:
                if char in freq_map:
                    n = freq_map[char]
                    n = n + 1
                    freq_map[char] = n
                else:
                    freq_map[char] = 1
            fset = frozenset(freq_map.items())
            if fset in seen:
                idx = seen_to_idx[fset]
                anagram_list = anagram_l_list[idx]
                anagram_list.append(elem)
            else:
                seen.add(fset)
                seen_to_idx[fset] = pos
                anagram_l_list.insert(pos, [elem])
                pos += 1
        return anagram_l_list

