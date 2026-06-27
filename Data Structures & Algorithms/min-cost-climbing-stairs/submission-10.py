class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # pattern: top down memoization
        dp = [-1] * len(cost)

        def dfs(i):
            # base case: out of bounds
            if i >= len(cost):
                return 0
            # memo check
            if dp[i] != -1:
                return dp[i]
            # recursion
            dp[i] = cost[i] + min(
                # pay for cur step
                # either take 1 step or 2 step
                dfs(i + 1),
                dfs(i + 2),
            )
            return dp[i]

        return min(dfs(0), dfs(1))
