class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # idea: prefix sum
        pfx = [0] * len(nums)
        sfx = [0] * len(nums)
        res = [0] * len(nums)

        # initialize with 1
        pfx[0] = 1
        sfx[len(nums) - 1] = 1

        # pfx: start from left, start at 2nd left
        for i in range(1, len(nums)):
            pfx[i] = pfx[i - 1] * nums[i - 1]

        # sfx: start from 2nd right, stop before 0, -1 index
        for i in range(len(nums) - 2, -1, -1):
            sfx[i] = sfx[i + 1] * nums[i + 1]

        # total: pfx * sfx = total sum
        for i in range(len(nums)):
            res[i] = pfx[i] * sfx[i]

        return res
