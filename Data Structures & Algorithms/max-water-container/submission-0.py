class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxArea = float("-inf")
        while i < j:
            d = j - i
            h = min(heights[i], heights[j])
            maxArea = max(maxArea, d * h)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maxArea
        