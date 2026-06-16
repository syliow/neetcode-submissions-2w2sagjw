class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0

        # pattern: dfs: start from top left (r: 0, c: 0)
        # idea: directly modify grid
        def dfs(r, c):
            # base case: out of bounds
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == "0":
                return

            grid[r][c] = "0"  # mark as visited
            # go for 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # go thru each grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count
