class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # pattern: djikstra
        n = len(grid)
        visit = set()
        minHeap = [[grid[0][0], 0, 0]]  # (time/ max height, r, c)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        visit.add((0, 0))
        while minHeap:
            h, r, c = heapq.heappop(minHeap)
            # reach btm right
            if r == n - 1 and c == n - 1:
                return h
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr == n or nc < 0 or nc == n or (nr, nc) in visit:
                    continue
                visit.add((nr, nc))
                # check current height vs nei height
                heapq.heappush(minHeap, [max(h, grid[nr][nc]), nr, nc])
