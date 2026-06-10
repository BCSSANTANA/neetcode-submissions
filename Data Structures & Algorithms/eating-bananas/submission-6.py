class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minK = r
        if self.valid(l, piles, h):
            return l
        while l <= r:
            c = (r + l) // 2
            if self.valid(c, piles, h):
                if c < minK:
                    minK = c
                r = c - 1
            else:
                l = c + 1
        return minK


    def valid(self, k: int, piles: List[int], h: int) -> bool:
        slices = 0
        for p in piles:
            slices +=  -(p // -k) # takes the celing of p // k
            if slices > h:
                return False
        return True