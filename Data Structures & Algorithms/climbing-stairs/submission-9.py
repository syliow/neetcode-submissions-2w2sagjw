class Solution:
    def climbStairs(self, n: int) -> int:
        # pattern: btm up (R -> L)
        dp = [0] * (n + 1)
        dp[n] = 1  # only 1 way at top
        dp[n - 1] = 1  # only 1 way to top

        for i in range(n - 2, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]  # either climb 1 or 2 steps
        return dp[0]
