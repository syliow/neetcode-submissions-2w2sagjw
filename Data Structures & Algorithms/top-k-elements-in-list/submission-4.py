class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = Counter(nums)
        minHeap = [(count, num) for num, count in numCount.items()]
        heapq.heapify(minHeap)

        while len(minHeap) > k:
            heapq.heappop(minHeap)

        # now minheap contains the topk freq ele
        res = []
        while minHeap:
            _, num = heapq.heappop(minHeap)
            res.append(num)
        return res
