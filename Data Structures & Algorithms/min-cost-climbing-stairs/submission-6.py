class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # pattern: btm up approach
        n = len(cost)
        dp = [0] * (n + 1)
        # base case
        # start from 2nd last
        for i in range(2, n + 1):
            # <---- prev1 , prev2
            # rmb to add current cost for the current stair
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        # return either index 0 or 1 (chepaer ones)
        return dp[n]
