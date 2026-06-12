class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [(0, 0)]
        visited = set()
        totalCost = 0

        n = len(points)
        adj = defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                # calculate manhanttan dist
                distance = abs(x1 - x2) + abs(y1 - y2)
                # push to adj list
                adj[i].append([distance, j])
                adj[j].append([distance, i])
        # prim
        while minHeap:
            cost, i = heapq.heappop(minHeap)
            # if the point is already visited, skip it
            if i in visited:
                continue
            visited.add(i)
            totalCost += cost
            # check neighbor
            for neiCost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neiCost, nei])
        return totalCost
