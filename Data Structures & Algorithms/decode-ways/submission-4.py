class Solution:
    def numDecodings(self, s: str) -> int:
        # pattern: btm up approach
        # step by step, from easiest idea
        # end of str = how many ways we can form

        # base case: 1 length or starts with 0
        if len(s) == 0 or s[0] == "0":
            return 0

        # setup dp
        n = len(s)
        dp = [0] * (n + 1)

        dp[0] = 1  # base case: do nothing also count as 1 decode way
        dp[1] = 1

        # for loop to update dp[i]
        # 2 choice: single digit or double digit
        for i in range(2, n + 1):
            # choice 1: single digit (look back 1 step)
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            # choice 2: double digit (look back 2 step)
            # either is 1X or 2X (within 26)
            if s[i - 2] == "1" or (s[i - 2] == "2" and s[i - 1] in "0123456"):
                dp[i] += dp[i - 2]

        return dp[-1]
