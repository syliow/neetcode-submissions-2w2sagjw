class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # pattern: find closest to origin : minheap
        # we need distance from origin -> our point
        # formula: (x1 - x2)^2 + (y1 - y2)^2
        # origin is 0, 0
        # formula = (x1 - 0)^2 + (y1 - 0)^2
        # Final formula = (x1 ^2) + (y1 ^2)

        minHeap = []
        heapq.heapify(minHeap)
        res = []

        for v in points:
            x1 = v[0]
            y1 = v[1]
            distance = (x1**2) + (y1**2)  # ** = power
            # push back the calculated distanced to heap
            heapq.heappush(minHeap, [distance, x1, y1])

        # check len of res against k
        while len(res) < k:
            distance, x, y = heapq.heappop(minHeap)
            res.append([x, y])

        return res
