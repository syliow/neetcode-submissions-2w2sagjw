class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # pattern: multi source bfs (find min path)
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        q = deque()

        # start bfs from treasure chest first, add to q
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:  # treasure
                    q.append([r, c])

        # once we have queue, we process all together
        while q:
            r, c = q.popleft()
            # 4 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # check boundaries and if its an unvisited land cell (INF)
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 2147483647:
                    #neiRow, neiCol = oldRow, oldCol + 1
                    grid[nr][nc] = grid[r][c] + 1
                    q.append([nr, nc])
