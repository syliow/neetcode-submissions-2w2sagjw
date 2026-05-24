class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        res = []
        pac, atl = set(), set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        # visit is which ocean we are visiting
        def dfs(r, c, visit, prevHeight):
            # base case: invalid scenario
            if (
                min(r, c) < 0
                or r >= ROWS
                or c >= COLS
                or
                # water can only flow to equal height or lower
                (r, c) in visit
                or heights[r][c] < prevHeight
            ):
                return

            # include
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])

        # Loop through columns to scan top and bottom edges
        for c in range(COLS):
            # Top edge: Row 0, Column c -> Pacific
            dfs(0, c, pac, heights[0][c])
    
            # Bottom edge: Last row, Column c -> Atlantic
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # Loop through rows to scan left and right edges
        for r in range(ROWS):
            # Left edge: Row r, Column 0 -> Pacific
            dfs(r, 0, pac, heights[r][0])
            # Right edge: Row r, Last column -> Atlantic
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # go thru every single pos in grid
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
