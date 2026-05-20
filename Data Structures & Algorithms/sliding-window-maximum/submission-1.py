class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # pattern: deque
        # compare against top deque
        # if num > top deque = popleft
        # if num < top deque = push

        res = []  # to store index of possible max
        l, r = 0, 0
        q = deque()

        while r < len(nums):
            # compare nums[r] vs top stack
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            # if number out of bounds
            if l > q[0]:
                q.popleft()

            # window size == k ,add to res
            if (r + 1) >= k:
                res.append(nums[q[0]])
                # update pointer
                l += 1
            r += 1
        return res
