class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = {}

        def dfs(i, openN):
            # base case: too many close brackets
            if openN < 0:
                return False
            # base case: reached end of string
            if i == len(s):
                return openN == 0
            # memo check
            if (i, openN) in dp:
                return dp[(i, openN)]

            # recursion
            if s[i] == "(":
                res = dfs(i + 1, openN + 1)
            elif s[i] == ")":
                res = dfs(i + 1, openN - 1)
            else:
                # handle "*" choices
                res = dfs(i + 1, openN) or dfs(i + 1, openN + 1) or dfs(i + 1, openN - 1)
            dp[(i, openN)] = res
            return res

        return dfs(0, 0)
