class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # pattern: min heap
        minHeap = []
        res = []

        for x1, y1 in points:
            # distance
            dist = (x1 - 0) ** 2 + (y1 - 0) ** 2
            heapq.heappush(minHeap, [dist, x1, y1])

        while k > 0:
            [_, x, y] = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res
