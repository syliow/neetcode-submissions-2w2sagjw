class Solution:
    def numDecodings(self, s: str) -> int:
        # pattern: DP, top down memoization
        # subproblem: we only decode curr digit (single) or decode double digit (include next)
        # cannot start with 0
        dp = [-1] * len(s)

        def dfs(i):
            # base case: went thru all charas
            if i == len(s):
                return 1
            # early return if it starts with 0
            if s[i] == "0":
                return 0
            # memo check
            if dp[i] != -1:
                return dp[i]
            # recursion
            # handle single digit
            # issue: how do we declare eg alphabet -> num mapping
            # issue 2: how do we check for digits
            res = 0

            res += dfs(i + 1)
            # handle double digit
            if i + 1 < len(s):
                twoDigits = int(s[i : i + 2])
                if 10 <= twoDigits <= 26:
                    res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)
