class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # pattern: prioritize based on count, greedy / max heap
        # pattern2: cooldown / waiting -> queue
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]  # handle high freq task first
        heapq.heapify(maxHeap)
        q = deque()  # pairs of [-cnt, idleTime]
        time = 0

        # process a task / check cooldown q
        while maxHeap or q:
            # every action = 1 time
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)  # +1 bcs we using maxheap
                if cnt:
                    q.append([cnt, time + n])
            else:
                time = q[0][1]
            # cooldown finished, push back to maxheap again to process
            if q and q[0][1] == time:
                newCount = q.popleft()[0]
                heapq.heappush(maxHeap, newCount)
        return time
