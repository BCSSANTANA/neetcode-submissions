class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = float('inf')
        while l <= r:
            c = (l + r) // 2
            m = min(m, nums[c], nums[r], nums[l])
            if nums[c] > nums[l] or nums[c] > nums[r]:
                l = c + 1
            else:
                r = c - 1
        return m