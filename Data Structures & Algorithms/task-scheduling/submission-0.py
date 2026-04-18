class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #create a freq map: eg (X: 2, Y: 3)
        #higher count = higher priority
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0 #time = cooldown
        q = deque() #cooldown queue, push back to heap after cd
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1] #[-cnt, idleTime]
            else:
                #pop the task with largest count
                # +1 bcs maxheap negative
                cnt = 1 + heapq.heappop(maxHeap)

                #if still have remaining
                #push back to q with new time
                if cnt:
                    q.append([cnt, time + n])
            #cd finish, push back to heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time