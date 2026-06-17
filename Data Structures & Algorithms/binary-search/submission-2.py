class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #pattern: sorted in asc, target, log n time -> binary search
        l, r = 0, len(nums) - 1
        while l <= r: #we are searching for a target, not range
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l += 1
            elif nums[mid] > target:
                r -= 1
        return -1 #fallback