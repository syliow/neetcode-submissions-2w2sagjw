class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dp = {}

        def dfs(r, c, prev):
            # base case
            if r < 0 or c < 0 or r == ROWS or c == COLS or matrix[r][c] <= prev:
                return 0
            # memo check
            if (r, c) in dp:
                return dp[(r, c)]
            # recursion
            res = 1
            for dr, dc in directions:
                row, col = r + dr, c + dc
                res = max(res, 1 + dfs(row, col, matrix[r][c]))
            dp[(r, c)] = res
            return res

        # go through entire grid
        maxPath = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxPath = max(maxPath, dfs(r, c, float("-inf")))
        return maxPath