class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def dfs(i, j):
            # base case: success
            if j == len(t):
                return 1

            # base case: run out of charas (invalid)
            if i == len(s):
                return 0

            # memo check
            if (i, j) in dp:
                return dp[(i, j)]

            # recursion
            # either include or skip current chara to form the subsequences
            res = 0
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)  # include chara bcs both match
            res += dfs(i + 1, j) #skip

            dp[(i, j)] = res
            return res

        return dfs(0, 0)
