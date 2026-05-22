class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #min cycle = max heap (focus on task with highest count)
        #one cycle = all task run once
        #cycle -> idle -> cycle -> idle
        #prioritize task with highest count
        count = Counter(tasks)
        
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0
        #as long freqmap got count we push to maxheap
        while maxHeap or q:
            time += 1 #cooldown time

            if not maxHeap:
                time = q[0][1] #grab the time from front q
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                #if we still have count, push back to q
                if cnt:
                    q.append([cnt, time + n])

            #edge cases: maxheap empty , q got task
            #edge cases: move task from queue to heap
            #push back the latest task to heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
                
