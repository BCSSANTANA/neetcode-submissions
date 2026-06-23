class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = float('infinity')
        maxProfit = 0
        for p in prices:
            if p < smallest:
                smallest = p
            if p - smallest > maxProfit:
                maxProfit = (p - smallest)
        return maxProfit

        