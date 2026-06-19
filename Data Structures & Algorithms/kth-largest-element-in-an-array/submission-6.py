class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # get sorted order without sorting
        # pattern: minheap
        minHeap = []
        # a heap only guarantees the top value, so we need loop
        for n in nums:
            heapq.heappush(minHeap, n)
            #if heap > k, pop it
            if len(minHeap) > k:
                heapq.heappop(minHeap) #now kth smallest is always at top
        return minHeap[0]