class Solution:
    def climbStairs(self, n: int) -> int:
        # pattern: btm up (R -> L)
        dp = [0] * (n + 1)
        # only 1 way for top and 1 step before top to reach top
        dp[-1] = 1
        dp[-2] = 1

        for i in range(n - 2, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]
