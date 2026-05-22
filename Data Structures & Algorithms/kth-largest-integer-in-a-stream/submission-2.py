class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #minheap
        self.minHeap = nums
        self.k = k

        #initialize the heap first
        #heapify is much faster
        heapq.heapify(self.minHeap)
     
        #push first, make sure its within count later
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        #add first , pop later
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
        
