class Solution:
    def numDecodings(self, s: str) -> int:
        # cannot lead with zero
        # pattern: btm up approach (L -> R) follow sequence
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1

        # start from r -> l
        for i in range(len(s) - 1, -1, -1):
            # base case
            if s[i] == "0":
                dp[i] = 0
                continue

            # handle 1 digit
            dp[i] = dp[i + 1]

            # handle 2 digit
            # handle 1X (10 - 19)
            # handle 2X (20 - 26)
            if i + 1 < len(s) and 10 <= int(s[i : i + 2]) <= 26:
                dp[i] += dp[i + 2]  # add ans on top, not replace
        return dp[0]
