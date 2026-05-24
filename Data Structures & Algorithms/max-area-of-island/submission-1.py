class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # pattern: DFS, we need to explore every path
        # core idea: 1 grid = 1 area , we need to get max island area
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        maxArea = 0  # compare maxArea vs area in path
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            currentArea = 0  # island area in path
            # base case: when do we stop dfs moving
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 0:
                return 0

            # core idea of dfs(include, backtrack, exclude)
            visited.add((r, c))
            currentArea += 1
            # mark visited island as water to avoid revisit
            grid[r][c] = 0

            # backtrack
            for dr, dc in directions:
                currentArea += dfs(r + dr, c + dc)

            # before we end dfs loop, compare max vs current
            return currentArea

        # loop thru whole grid
        for r in range(ROWS):
            for c in range(COLS):
                # only loop thru land
                if grid[r][c] == 1:
                    # compare island area
                    maxArea = max(maxArea, dfs(r, c))
        return maxArea
