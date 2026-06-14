class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pattern: prefix, suffix
        n = len(nums)
        pfx = [0] * n
        sfx = [0] * n
        res = [0] * n

        pfx[0] = 1
        sfx[-1] = 1

        # pfx: starts at 1, skip 0
        for i in range(1, n):
            pfx[i] = pfx[i - 1] * nums[i - 1]

        # sfx: starts from last 2nd index, skip last
        for i in range(n - 2, -1, -1):
            sfx[i] = sfx[i + 1] * nums[i + 1]

        # res = sfx * pfx
        for i in range(n):
            res[i] = pfx[i] * sfx[i]

        return res
