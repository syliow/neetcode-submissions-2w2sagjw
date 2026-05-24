class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # pattern: multi source BFS
        # idea: collect all starting point initially
        # queue, process 1 by 1
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        q = deque()
        time = 0
        freshOrange = 0

        # collect all starting point initially
        for r in range(ROWS):
            for c in range(COLS):
                # count fresh orange
                if grid[r][c] == 1:
                    freshOrange += 1

                # start from rotten oren
                if grid[r][c] == 2:
                    q.append([r, c])

        def bfs(r, c):
            nonlocal freshOrange
            # base case: invalid scenario
            if (
                min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1  # ignore empty or rot
            ):
                return
            # spread the rot 
            grid[r][c] = 2
            q.append([r, c])
            freshOrange -= 1

        # q not empty
        while q:
            for i in range(len(q)):
                # process element
                r, c = q.popleft()  # FIFO
                # oren is already rotten in q
                # spread to 4 directions
                for dr, dc in directions:
                    bfs(r + dr, c + dc)
            # only increment time if we found fresh oren -> rot oren
            if q:
                time += 1
        return time if freshOrange == 0 else -1
