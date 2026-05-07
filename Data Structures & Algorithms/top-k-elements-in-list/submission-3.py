class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        SORTED = False
        for n in nums:
            if n in d:
                i = d[n]
                i += 1
                d[n] = i
            else:
                d[n] = 1
        l = sorted(d, key=d.get)
        c = 1
        i = len(l) - 1
        ans = []
        print(l)
        while c <= k  and i >= 0:
            ans.append(l[i])
            i -= 1
            c += 1
        return ans
