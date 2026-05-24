class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # pattern: multi source bfs: queue
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()

        def bfs(r, c):
            # base case: invalid conditions
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == -1:
                return
            # initialize all starting point at first
            visited.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:  # start move from treasure chest
                    q.append([r, c])
                    visited.add((r, c))

        dist = 0
        while q:  # if queue not empty, move nodes
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist  # directly mark dist in grid
                for dr, dc in directions:
                    bfs(r + dr, c + dc)
            dist += 1
