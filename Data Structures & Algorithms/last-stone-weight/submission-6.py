class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # keyword: 2 heaviest stones
        # maxheap use negative
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            # top 2 stones
            stone1 = heapq.heappop(maxHeap)
            stone2 = heapq.heappop(maxHeap)
            diff = stone1 - stone2

            if stone1 != stone2:
                heapq.heappush(maxHeap, diff)

        return 0 if len(maxHeap) == 0 else -maxHeap[0]
