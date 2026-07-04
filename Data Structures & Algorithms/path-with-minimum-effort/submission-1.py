class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # pattern: djikstra algo
        # shortest path from top left to btm right
        # idea: minheap, visited set
        ROWS, COLS = len(heights), len(heights[0])
        minHeap = [[0, 0, 0]]  # diff, row , col
        visited = set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue
            visited.add((r, c))

            # base case: reach btm right (goal)
            if r == ROWS - 1 and c == COLS - 1:
                return diff

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                # base case
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in visited:
                    continue

                newDiff = max(diff, abs(heights[nr][nc] - heights[r][c]))
                # push back q to process
                heapq.heappush(minHeap, [newDiff, nr, nc])

        return 0  # fallback