class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #minheap
        minHeap = list(nums)
        heapq.heapify(minHeap)
        res = []

        for _ in range(len(nums)):
            val = heapq.heappop(minHeap)
            res.append(val)
        
        return res