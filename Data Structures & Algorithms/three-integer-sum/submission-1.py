class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        seen = []
        for i in range(len(sortedNums)):
            s = 0
            e = len(sortedNums) - 1
            add = float('inf')
            while s < e:
                if s != i and e != i and e != s:
                    add = sortedNums[s] + sortedNums[i] + sortedNums[e]
                    if add == 0:
                        s_l = sorted([sortedNums[s], sortedNums[i], sortedNums[e]])
                        if s_l not in seen:
                            seen.append(s_l)
                        e -= 1
                    elif add > 0:
                        e -= 1
                    else:
                        s += 1
                elif s == i:
                    s += 1
                else:
                    e -= 1
        return seen
