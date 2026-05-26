class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # pattern: prim algo
        N = len(points)
        # create adj list
        adj = {i: [] for i in range(N)}  # list of [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                # formula
                dist = abs(x1 - x2) + abs(y1 - y2)

                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prims algo
        res = 0
        visit = set()
        minHeap = [[0, 0]]  # start from 0 [cost, point]
        while len(visit) < N:
            # pop add to set
            cost, i = heapq.heappop(minHeap)
            # might have dup, so we want to skip dup
            if i in visit:
                continue
            visit.add(i)
            res += cost
            # continue search for nei
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])
        return res
