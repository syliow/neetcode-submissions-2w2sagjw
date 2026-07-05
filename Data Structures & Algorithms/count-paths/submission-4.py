class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m is cols , n is rows
        dp = {}  # (r, c)
        visited = set()

        def dfs(r, c):
            # base case
            if r < 0 or c < 0 or r == n or c == m or (r, c) in visited:
                return 0
            # base case : reach goal
            if r == n - 1 and c == m - 1:
                return 1

            # memo check
            if (r, c) in dp:
                return dp[(r, c)]
            # recursion
            # go down or go right
            res = 0  # total path
            res += dfs(r + 1, c) + dfs(r, c + 1)
            dp[(r, c)] = res
            return res

        return dfs(0, 0)
