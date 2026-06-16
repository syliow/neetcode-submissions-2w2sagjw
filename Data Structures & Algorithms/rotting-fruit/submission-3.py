class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # pattern: multi source bfs
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        q = deque()
        fresh = 0
        time = 0
        # dunnid visit set bcs we can directly modify grid
        # initialization of bfs
        for r in range(ROWS):
            for c in range(COLS):
                # count fresh oren
                if grid[r][c] == 1:
                    fresh += 1
                # count rot oren
                if grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                # how to check adjacent rot oren
                for dr, dc in directions:
                    row, col = r + dr, c + dc  # neighbor row, neighbor col
                    # base case: check in bounds
                    if row in range(ROWS) and col in range(COLS) and grid[row][col] == 1:
                        # rot it and add to q
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row, col))
            time += 1
        return time if fresh == 0 else -1
