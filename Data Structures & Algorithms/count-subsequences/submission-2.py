class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def dfs(i, j):
            # base case
            if j == len(t):
                return 1
            # run out of charas
            if i == len(s):
                return 0

            # memo check
            if (i, j) in dp:
                return dp[(i, j)]

            # recursion
            res = 0
            # either both chara match or we skip i to check next
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            res += dfs(i + 1, j)  # skip chara
            dp[(i, j)] = res
            return res

        return dfs(0, 0)
