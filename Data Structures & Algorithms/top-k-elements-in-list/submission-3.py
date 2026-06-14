class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        # min heap: bcs we pop all smallest val and remaining is large
        minHeap = []
        res = []
        for num in count.keys():
            heapq.heappush(minHeap, (count[num], num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        for i in range(k):
            _, val = heapq.heappop(minHeap)
            res.append(val)
        return res
