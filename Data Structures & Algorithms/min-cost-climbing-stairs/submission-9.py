class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # pattern: btm up appraoch (R -> L)
        n = len(cost)
        dp = [0] * (n + 1)
        # base case, when we are at top first step have 0 cost
        dp[n] = 0
        dp[n - 1] = cost[n - 1]

        for i in range(n - 2, -1, -1):
            # R-> L is +
            # 2 choice: either 1 step or 2 step
            # pay current step cost + eithet next step or next 2 step price
            dp[i] = min(cost[i] + dp[i + 1], cost[i] + dp[i + 2])
        # bcs we can stop at either last or 2nd last step
        return min(dp[0], dp[1])
