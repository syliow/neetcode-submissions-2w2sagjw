class Solution:
    def numDecodings(self, s: str) -> int:
        # pattern: brute force -> top down (recursion)
        # idea: how many ways we can decide string at index i
        memo = [-1] * len(s)

        def dfs(i):
            # base case: valid decoding
            if i == len(s):
                return 1
            # must not start with 0
            if s[i] == "0":
                return 0  # 0 ways

            # memo check
            if memo[i] != -1:
                return memo[i]

            # recursion
            # TLDR: either we grab single chara, or duo chara (current + next)
            memo[i] = dfs(i + 1)
            # make sure i is still within bounds
            if i < len(s) - 1:
                # only proceed if it starts with either 1 or 2
                if (
                    s[i] == "1"
                    or
                    # stay within 26
                    s[i] == "2"
                    and s[i + 1] < "7"
                ):
                    memo[i] += dfs(i + 2)
            return memo[i]

        return dfs(0)
