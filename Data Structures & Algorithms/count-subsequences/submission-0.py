class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # pattern: recursion dfs
        # idea: check s[i] against t[i], if match, we move on to check next i until end of len t
        # only if everything passes only we add 1 to res
        dp = {}  # (i, j) = num

        def dfs(i, j):
            # base case
            if j == len(t):
                return 1

            # out of bounds
            if i >= len(s):
                return 0

            # check memo
            if (i, j) in dp:
                return dp[(i, j)]

            # recursion
            # theres 2 option: either we take current chara or skip cur
            res = 0
            # both move forward to continue check next pair
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            # if skip cur
            res += dfs(i + 1, j)
            # assign to dp
            dp[(i, j)] = res
            return res

        return dfs(0, 0)
