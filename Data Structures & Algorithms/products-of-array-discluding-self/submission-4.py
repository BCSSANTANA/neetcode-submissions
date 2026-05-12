class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ZERO_LIMIT = 1
        n_z = 0
        l_prod = 1
        t_prod = 1
        for n in nums:
            t_prod *= n
            if n == 0:
                n_z += 1

            if n != 0 and n_z <= ZERO_LIMIT:
                l_prod *= n
            elif n_z > ZERO_LIMIT:
                l_prod = 0
        output = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                output[i] = t_prod // nums[i]
            elif l_prod != 0:
                output[i] = l_prod
            else:
                output[i] = 0
        return output
