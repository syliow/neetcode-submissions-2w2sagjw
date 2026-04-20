class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #pattern: quick select
        target = len(nums) - k
        l, r = 0 , len(nums) - 1

        while (l <= r):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p == target:
                return nums[p]
            elif p < target: #move right
                l = p + 1
            else: #move L
                r = p - 1