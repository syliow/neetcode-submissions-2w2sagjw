class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def dfs(i):
            # subproblem : either rob cur or skip cur
            if i >= len(nums):
                return 0
            # memo check
            if dp[i] != -1:
                return dp[i]
            # recursion
            dp[i] = max(
                dfs(i + 2) + nums[i],  # rob cur
                dfs(i + 1),  # skip cur
            )
            return dp[i]

        return dfs(0)
