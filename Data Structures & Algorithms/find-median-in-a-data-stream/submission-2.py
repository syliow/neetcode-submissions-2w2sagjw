class MedianFinder:
    def __init__(self):
        self.small = []  # max heap
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        # make sure every num small is <= every num in large
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        # uneven size
        # 3 vs 1
        if len(self.small) - len(self.large) > 1:
            # push to large(min)
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # 1 vs 3
        if len(self.large) - len(self.small) > 1:
            # push to small (max)
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # odd num: we get from whichever side has longer length
        if len(self.small) > len(self.large):
            return -1 * self.small[0]  # maxheap
        elif len(self.large) > len(self.small):
            return self.large[0]  # min heap
        else:
            # even num
            return (-1 * self.small[0] + self.large[0]) / 2
