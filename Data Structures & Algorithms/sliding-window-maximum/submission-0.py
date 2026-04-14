class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() #store index instead of value
        l = r = 0

        while r < len(nums):
            #compare latest num against back of deque
            while q and nums[q[-1]] < nums[r]:
                q.pop() #pop the num from q if its smaller
            q.append(r)

            #if it goes out of win size
            if l > q[0]:
                q.popleft()

            #ensure its at correct win size
            if (r + 1) >= k:
                #the queeue contains index of largest num in window
                output.append(nums[q[0]])
                l += 1
            #move to next window
            r += 1

        return output
