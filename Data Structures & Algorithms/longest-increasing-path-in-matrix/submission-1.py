class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # idea: go through from each grid pos
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # r, c

        def dfs(r, c, prev):
            # out of bounds
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or matrix[r][c] <= prev:
                return 0

            # memo check
            if (r, c) in dp:
                return dp[(r, c)]

            # recursion
            # go thru all 4 directions, only plus 1 if the next val is > cur val
            res = 1  # base is 1

            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

            dp[(r, c)] = res
            return res

        # go through each grid
        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, float("-inf"))
        # start at top left
        return max(dp.values())
