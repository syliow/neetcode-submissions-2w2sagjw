class Solution:
    def numDecodings(self, s: str) -> int:
        # pattern: btm up approach (r -> L)
        # subproblem: how many ways can i decode a msg at index i?
        # <----- R- L

        n = len(s)
        dp = [0] * (n + 1)

        dp[n] = 1  # single chara is always 1

        for i in reversed(range(n)):
            # make sure first digit doesnt start with 0
            # it should only start with either 1 / 2
            # and 2nd digit should be in "123456" for 20s
            if s[i] == "0":
                dp[i] = 0
            else:
                # decode single digit
                dp[i] = dp[i + 1]

            # case 2: decode double digit
            if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]

        return dp[0]
