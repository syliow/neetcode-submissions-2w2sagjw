class Solution:
    def rob(self, nums: List[int]) -> int:
        #pattern: top down memoization dp
        n = len(nums)
        dp = [-1] * (n + 1)

        def dfs(i):
            #base case
            if i >= n:
                return 0
            #memo check
            if dp[i] != -1:
                return dp[i]
            #recursion
            robCur = dfs(i + 2) + nums[i]
            skipCur = dfs(i + 1)
            dp[i] = max(robCur, skipCur)
            return dp[i]

        return dfs(0)