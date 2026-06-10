class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        elif nums[mid] == target:
            return mid
        while l < r:
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            mid = (l + r) // 2
        return -1

            


