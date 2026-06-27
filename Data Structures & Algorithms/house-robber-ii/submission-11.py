class Solution:
    def rob(self, nums: List[int]) -> int:
        # pattern: 0 1 knapsack
        # skip first or skip last
        if len(nums) == 1: return nums[0]
        n = len(nums)
        
        def dfs(i, houses, dp):
            # base case: out of bounds
            if i >= len(houses):
                return 0
            # memo check
            if dp[i] != -1:
                return dp[i]
            # recursion
            # rob current or skip current
            robCurr = dfs(i + 2, houses, dp) + houses[i]
            skipCurr = dfs(i + 1, houses, dp)
            dp[i] = max(robCurr, skipCurr)
            return dp[i]

        res1 = dfs(0, nums[1:], [-1] * n) #skip first
        res2 = dfs(0, nums[:-1], [-1] * n) #skip last
        return max(res1, res2)