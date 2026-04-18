class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #remove 2 heaviest stone = maxheap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
            #in case no more stones
        stones.append(0)
        return abs(stones[0])