class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #pattern: heap
        minHeap = []
        #initialize the minheap
        for i in range(k):
            heapq.heappush(minHeap, nums[i])
        #process elements from k to end of arr
        for i in range(k, len(nums)):
            #if the current number is larger than our smallest heap
            if nums[i] > minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, nums[i])
        return minHeap[0]