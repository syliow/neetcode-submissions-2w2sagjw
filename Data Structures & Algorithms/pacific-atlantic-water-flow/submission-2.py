class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        # if nei.val <= cur.val, flow
        pcf, atl = set(), set()
        res = []

        # pattern: dfs
        def dfs(r, c, ocean, prevHeight):
            # base case
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or (r, c) in ocean
                or heights[r][c] < prevHeight 
            ):
                return
            ocean.add((r, c))
            # go through nei
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])

        # top and btm border
        for col in range(COLS):
            # top
            dfs(0, col, pcf, heights[0][col])
            # btm
            dfs(ROWS - 1, col, atl, heights[ROWS - 1][col])
        # left and right border
        for row in range(ROWS):
            # left
            dfs(row, 0, pcf, heights[row][0])
            # right
            dfs(row, COLS - 1, atl, heights[row][COLS - 1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pcf and (r, c) in atl:
                    res.append([r, c])
        return res