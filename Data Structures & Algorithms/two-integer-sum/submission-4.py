class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}
        for i in range(len(nums)):
            if nums[i] in num_to_idx:
                idx_list = num_to_idx[nums[i]]
                idx_list.append(i)
            else:
                num_to_idx[nums[i]] = [i]
        nums.sort()
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                FIRST_IDX = 0
                SECOND_IDX = 1
                if nums[i] == nums[j]:
                    k = num_to_idx[nums[i]][FIRST_IDX]
                    j = num_to_idx[nums[j]][SECOND_IDX]
                    if k > j:
                        return [j, k]
                    else:
                        return [k, j]
                else:
                    k = num_to_idx[nums[i]][FIRST_IDX]
                    j = num_to_idx[nums[j]][FIRST_IDX]
                    if k > j:
                        return [j, k]
                    else:
                        return [k, j]
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        return False
