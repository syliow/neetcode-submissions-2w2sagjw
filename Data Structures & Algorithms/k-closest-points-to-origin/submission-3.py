class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #pattern: minHeap, find the closest point to origin
        #[dist to origin, x1, y1]
        minHeap = []
        res = []
        for x1, y1 in points:
            distance = (x1 - 0) ** 2 + (y1 - 0) ** 2 
            heapq.heappush(minHeap, (distance, x1, y1))
        
        for _ in range(k):
            [distance, x1, y1] = heapq.heappop(minHeap)
            res.append([x1, y1])
        return res