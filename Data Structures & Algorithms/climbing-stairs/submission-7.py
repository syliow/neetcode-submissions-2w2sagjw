class Solution:
    def climbStairs(self, n: int) -> int:
        # pattern: btm up approach (R -> L)

        dp = [0] * (n + 1)
        dp[-1] = 1
        dp[-2] = 1
        # <---------------------- n (2)
        # cur <- prev1 <- prev2
        # start from r move to l
        # start at last, stop before 0, -1 every iteration
        for i in range(n - 2, -1, -1):
            # dp[2] = d[3] + dp[4]
            dp[i] = dp[i + 1] + dp[i + 2]
            
        #final ans is stop at first index(0)
        return dp[0]
