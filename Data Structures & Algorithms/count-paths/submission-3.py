class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # pattern: 2d dp: why? bcs we are tracking both r and c at the same time
        # can only move right or down
        dp = {}  # (r, c)

        def dfs(r, c):
            # base case: valid scenario -> reach btm right
            if r == m - 1 and c == n - 1:
                return 1

            # base case: invalid scenario -> out of bounds
            if r < 0 or c < 0 or r > m or c > n:
                return 0

            # memo check
            if (r, c) in dp:
                return dp[(r, c)]

            # recursion: either move to right or down
            res = 0
            res = dfs(r + 1, c) + dfs(r, c + 1)
            dp[(r, c)] = res
            return res

        return dfs(0, 0)
