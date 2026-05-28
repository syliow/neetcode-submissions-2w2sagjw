class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # pattern: brute force -> top down dp
        # idea: cache results after calculating
        # subproblem: explore either jump 1 or 2 steps
        memo = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0
            # if -1 means its still counting
            if memo[i] != -1:
                return memo[i]
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]

        # start from 0 and 1
        return min(dfs(0), dfs(1))
