class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # initialization
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((t, v)) 
        minHeap = [[0, k]]  # (weight, node) <- start from k
        visited = set()
        totalTime = 0

        # start djikstra algo
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            #grab the shortest time and mark as visited
            totalTime = w1
            visited.add(n1)

            # check neighbor
            for w2, n2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return totalTime if len(visited) == n else -1
