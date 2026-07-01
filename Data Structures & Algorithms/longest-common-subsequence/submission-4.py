class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}  # [i, j]

        def dfs(i, j):
            # base case
            if j == len(text2):
                return 0
            if i == len(text1):
                return 0
            # memo check
            if (i, j) in dp:
                return dp[(i, j)]
            # recursion
            res = 0
            if text1[i] == text2[j]:
                res = 1 + dfs(i + 1, j + 1)
            else:
                # not equal
                res = max(dfs(i + 1, j), dfs(i, j + 1))
            dp[(i, j)] = res
            return res

        return dfs(0, 0)
