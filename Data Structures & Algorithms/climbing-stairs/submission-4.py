class Solution:
    def climbStairs(self, n: int) -> int:
        # bcs n and n-1 both returns n step
        if n <= 2:
            return n
        # pattern: btm up
        # btm up moves from right to left
        dp = [0] * (n + 1)  # index starts from 0 , so we need extra index
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
