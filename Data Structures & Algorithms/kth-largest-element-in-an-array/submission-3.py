class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #return largest element = max Heap
        #we can do it w/o sorting through maxheap
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)
        res = []

        #make sure heap is not empty and we get k element
        while maxHeap:
            #pop from heap and push to res
            #pop will always get the correct value (even heap might not be sorted)
            ele = heapq.heappop(maxHeap)
            res.append(-ele)
        
        return res[k - 1]