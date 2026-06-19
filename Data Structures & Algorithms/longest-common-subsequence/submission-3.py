class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # order is important but we can del charas
        # pattern: top down memoization
        dp = {}  # i, j

        def dfs(i, j):
            # invalid case: out of bounds
            if i == len(text1) or j == len(text2):
                return 0
            # memo check
            if (i, j) in dp:
                return dp[(i, j)]
            # recursion
            # base case: both chara at current index match
            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + dfs(i + 1, j + 1)
                return dp[(i, j)] 
            else:
                res = 0  # 2d dp so we use res
                res += max(dfs(i + 1, j), dfs(i, j + 1))
                dp[(i, j)] = res
                return res

        return dfs(0, 0)  # both starts from index 0
