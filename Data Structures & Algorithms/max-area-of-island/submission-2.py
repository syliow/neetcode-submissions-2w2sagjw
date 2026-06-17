class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # pattern: dfs
        # num of 1s = area
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            # base case
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0:
                return 0
            # starts from 1
            grid[r][c] = 0
            area = 0
            # look for neighbor
            return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)

        # look thru every grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = dfs(r, c)
                    maxArea = max(maxArea, res)
        return maxArea
