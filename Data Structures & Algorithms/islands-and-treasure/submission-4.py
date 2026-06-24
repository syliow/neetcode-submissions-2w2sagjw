class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # pattern: multi source BFS
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        # start from treasure first, add to q
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        def addCell(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == -1:
                return
            visited.add((r, c))
            grid[r][c] = dist + 1
            q.append([r, c])

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
