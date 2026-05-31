class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # pattern: recursion dfs
        # core idea: clear out everything on L and R before proceed with val i

        # always have 1 at front and back
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            # if out of bounds
            if l > r:
                return 0

            # memo check
            if (l, r) in dp:
                return dp[(l, r)]

            dp[(l, r)] = 0

            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]

        # first and last index is 1
        return dfs(1, len(nums) - 2)
