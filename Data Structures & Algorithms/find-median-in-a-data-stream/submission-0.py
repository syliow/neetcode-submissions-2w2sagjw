class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        #heaps should be equal size
        #small = maxHeap, large = minHeap

    def addNum(self, num: int) -> None:
        #make sure every num in small is <= in large
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num) #negative for maxheap

        #check for uneven size
        #diff between both <= 1, otherwise push to opp side
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        #side has longer length = contain median (odd)
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2
        
        