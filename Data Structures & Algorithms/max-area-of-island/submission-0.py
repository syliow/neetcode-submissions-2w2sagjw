class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #core idea: search for 4 directions
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            #base case
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS 
            or grid[r][c] == 0 or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))
        
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r, c))
        return maxArea