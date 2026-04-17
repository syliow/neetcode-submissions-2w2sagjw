class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #core idea: minheap = smallest val at front
        self.minHeap = nums
        self.k = k

        #heapify = make the list into actual minheap
        heapq.heapify(self.minHeap)
        #we need to keep track of kth
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        #add first , pop later
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
        
