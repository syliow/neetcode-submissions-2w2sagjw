class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #core idea: max heap
        #use -s for python (convert to negative)

        stones = [-s for s in stones]
        heapq.heapify(stones)

        #smash until only 1 stone remaining
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
               heapq.heappush(stones, first - second) 
        #return 0 if no stone remains
        stones.append(0)
        #turn negative back to positive
        return abs(stones[0])