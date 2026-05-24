class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # pattern: bfs (multi source)
        # collect starting point initially, run together step by step
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        q = deque()

        # scan the whole grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append([r, c])

        def bfs(r, c):
            # base case: invalid
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == -1:
                return False

            visited.add((r, c))
            q.append([r, c])

        dist = 0  # we want to directly update grid dist
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                # modify the grid
                grid[r][c] = dist
                for dr, dc in directions:
                    bfs(r + dr, c + dc)
            dist += 1
