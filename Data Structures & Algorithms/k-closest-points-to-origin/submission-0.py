class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #origin = [0, 0]
        #min heap = smallest distance always at front

        minHeap = []
        for x, y in points:
            #distance from origin
            dist = (x ** 2) + (y ** 2)
            #[distance, x, y]
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap)

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res