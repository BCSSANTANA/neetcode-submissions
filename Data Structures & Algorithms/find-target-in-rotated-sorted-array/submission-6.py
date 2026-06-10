class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        c = (l + r) // 2
        while l <= r:
            c = (l + r) // 2
            if nums[c]  == target:
                return c
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
        
            if nums[c] < nums[l] and (target > nums[l] or target < nums[c]):
                    r = c - 1
            elif nums[c] > nums[l] and target >= nums[l] and target <= nums[c]:
                    r = c - 1
            elif nums[c] > nums[r] and (target < nums[r] or target > nums[r]):
                    l = c + 1
            elif nums[c] < nums[r] and target >= nums[c] and target <= nums[r]:
                    l = c + 1
            else:
                return -1
        return -1