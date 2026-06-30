class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # pattern: DFS
        # idea: directly modify val in grid

        def dfs(r, c):
            # base case
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] != 1:
                return 0
            # go through 4 directions
            grid[r][c] = 0  # update to prevent re-visit
            res = 0
            res = 1 + (dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
            return res

        # go through every single grid
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                # dfs(r, c) returns each island size
                maxArea = max(maxArea, dfs(r, c))
        return maxArea
