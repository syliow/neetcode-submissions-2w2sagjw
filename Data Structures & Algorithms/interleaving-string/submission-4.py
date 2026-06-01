class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # idea: compare s1 and s2 against s3
        dp = {}  # {i, j, k} :

        def dfs(i, j, k):
            if len(s1) + len(s2) != len(s3):
                return False

            if i == len(s1) and j == len(s2):
                return True

            # base case: we checked until end of s3 = True
            if k == len(s3):
                return True if i == len(s1) and j == len(s2) else False

            # either i or j is out of bounds
            if i > len(s1) or j > len(s2):
                return False

            if (i, j, k) in dp:
                return dp[(i, j, k)]

            # recursion
            # either we grab the str from s1 or s2
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = dfs(i + 1, j, k + 1)
            #res become true in first recursion
            if j < len(s2) and s2[j] == s3[k]:
                res = dfs(i, j + 1, k + 1)

            dp[(i, j, k)] = res
            return res

        return dfs(0, 0, 0)
