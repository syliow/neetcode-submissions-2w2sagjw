class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case: only 1 house , rob it
        if len(nums) == 1:
            return nums[0]

        # top down memoization
        dp1 = [-1] * len(nums)
        dp2 = [-1] * len(nums)
        skipFirst = nums[1:]
        skipLast = nums[:-1]

        def dfs(i, houses, dp):
            # base case: out of bounds
            if i >= len(houses):
                return 0
            # memo check
            if dp[i] != -1:
                return dp[i]
            # recursion
            robCurrent = houses[i] + dfs(i + 2, houses, dp)
            skipCurrent = dfs(i + 1, houses, dp)
            dp[i] = max(robCurrent, skipCurrent)
            return dp[i]

        return max(dfs(0, skipFirst, dp1), dfs(0, skipLast, dp2))
