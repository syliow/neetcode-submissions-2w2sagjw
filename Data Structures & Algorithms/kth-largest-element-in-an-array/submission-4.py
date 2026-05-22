class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return largest element = max Heap
        # we can do it w/o sorting through maxheap
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)
        # make res into a num
        res = 0

        # # make sure heap is not empty and we get k element
        # while maxHeap and len(maxHeap) > k:
        #     # pop from heap and push to res
        #     # pop will always get the correct value (even heap might not be sorted)
        #     ele = heapq.heappop(maxHeap)
        #     res = -ele
        
        #OPTIMIZED SOLUTION
        for i in range(k):
            ele = heapq.heappop(maxHeap)
            res = -ele

        return res
