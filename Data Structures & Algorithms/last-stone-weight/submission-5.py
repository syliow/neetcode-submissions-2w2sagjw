class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        # smash top 2 stones
        while len(maxHeap) > 1:
            stone1 = -heapq.heappop(maxHeap)
            stone2 = -heapq.heappop(maxHeap)
            if stone2 < stone1:
                diff = stone1 - stone2
                heapq.heappush(maxHeap, -diff)
        return -maxHeap[0] if len(maxHeap) == 1 else 0