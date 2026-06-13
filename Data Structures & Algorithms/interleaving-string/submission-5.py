class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # pattern: 2d dp -> keep track of index from s1 and s2
        # top down memoization
        dp = {}  # [i, j] from s1 and s2

        def dfs(i, j):
            # base case: s1 + s2 == s3
            if len(s1) + len(s2) != len(s3):
                return False
            # base case: both s1 s2 reach end of str = ok
            if i == len(s1) and j == len(s2):
                return True

            # memo check
            if (i, j) in dp:
                return dp[(i, j)]
            res = False
            # recursion
            # core idea: check either i or j matches with k or not
            # s3 index = i + j, bcs we cannot skip

            # We either take from s1 or s2
            # take from s1
            if i < len(s1) and s1[i] == s3[i + j]:
                # res = dfs(i + 1, j) -> wrong bcs maybe overwrite true -> False
                res = res or dfs(i + 1, j)
            # take from s2
            if j < len(s2) and s2[j] == s3[i + j]:
                # res = dfs(i, j + 1) -> wrong bcs maybe overwrite true -> False
                res = res or dfs(i, j + 1)
            dp[(i, j)] = res
            return res

        return dfs(0, 0)
