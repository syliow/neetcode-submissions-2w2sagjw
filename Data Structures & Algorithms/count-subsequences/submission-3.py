class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # impossible if t is longer than s
        if len(t) > len(s):
            return 0

        dp = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            # base case: run out of charas
            if i == len(s):
                return 0
            # memo check
            if (i, j) in dp:
                return dp[(i, j)]
            # recursion
            res = 0
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            res += dfs(i + 1, j)
            dp[(i, j)] = res
            return res

        return dfs(0, 0)
