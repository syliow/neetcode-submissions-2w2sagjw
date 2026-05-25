class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # pattern : min heap
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))  # node: [path weight, target node]]
        minHeap = [[0, k]]  # path weight initial = 0, k is always starting ppomt
        visited = set()
        t = 0  # total time

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            # avoid cycle
            if n1 in visited:
                continue
            # otherwise add to visit
            visited.add(n1)
            t = w1  # 0 + w1 = w1

            # go through the neighbors
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    # push to q and process
                    # w1 + w2 is bcs total weight from node1 to node2
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visited) == n else -1
