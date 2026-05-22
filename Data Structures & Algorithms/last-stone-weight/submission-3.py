class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # pattern: we need to find 2 heaviest stone = maxheap
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) >= 2:
            stone1 = heapq.heappop(maxHeap)
            stone2 = heapq.heappop(maxHeap)
            diff = -abs(stone1 - stone2)

            if diff != 0:
                heapq.heappush(maxHeap, diff)

        #if leftover stone , len == 1
        #flip back from negative to positive
        return -maxHeap[0] if len(maxHeap) == 1 else 0
