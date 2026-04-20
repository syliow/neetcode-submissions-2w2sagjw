class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #core idea: look thru 4 directions to find 1
        directions = [
            [1, 0], [-1, 0],
            [0, 1], [0, -1]
        ]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0 #whenever we found 1 , add count to island

        def bfs(r, c):
            #bfs uses queue
            q = deque()
            #mark as visited
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    #check for invalid conditions
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS
                    or grid[nr][nc] == "0" ):
                        continue
                    
                    q.append((nr, nc))
                    grid[nr][nc] = "0" #mark nearby grid as visited

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands