class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # pattern: btm up approach (L -> R)
        n = len(cost)
        dp = [0] * (n + 1)

        # start at index 2, stop before n
        for i in range(2, n + 1):
            # can either skip 1 or skip 2
            #dp[i] = cache calculated prev cost + cost to move to next step
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        #dp[top of staircase]
        return dp[n]
