class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # pattern: 2d dp (recursion dfs)
        # idea: either move down or right
        # subproblem: do we move right or down

        # m = col / i
        # n = row / j
        dp = {}

        def dfs(i, j):
            res = 0
            # base case: stop when we reach btm right
            if i == m - 1 and j == n - 1:
                return 1 #1 path

            # base case: out of bounds
            if i < 0 or i > m - 1 or j < 0 or j > n - 1:
                return 0

            # memo check
            if (i, j) in dp:
                return dp[(i, j)]

            # recursion
            
            # go R
            res += dfs(i + 1, j)
            # go Down
            res += dfs(i, j + 1)
            dp[(i, j)] = res
            return res

        # we always start from top left -> btm right
        return dfs(0, 0)
