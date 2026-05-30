class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}

        def dfs(i, j, k):
            # prevent s3 out of bounds
            # What if s3 is actually longer than s1 and s2 combined?
            # s1 = "a"
            # s2 = "b"
            # s3 = "abc"
            if len(s1) + len(s2) != len(s3):
                return False
            # base case
            if i == len(s1) and j == len(s2):
                return True

            # dp check
            if (i, j) in dp:
                return dp[(i, j)]

            # recursion
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = dfs(i + 1, j, k + 1)
            if j < len(s2) and s2[j] == s3[k]:
                res = dfs(i, j + 1, k + 1)

            dp[(i, j)] = res
            return res

        return dfs(0, 0, 0)
