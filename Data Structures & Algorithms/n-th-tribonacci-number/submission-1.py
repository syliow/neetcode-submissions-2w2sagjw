class Solution:
    def tribonacci(self, n: int) -> int:
        #handle edge cases
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        # pattern: dp
        dp = [0] * (n + 1)  # need base case
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        # start from index 3 since first 2 index is defined
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]
