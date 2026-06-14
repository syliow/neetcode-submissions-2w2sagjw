class Solution:
    def findMin(self, nums: List[int]) -> int:
        # pattern: log n -> bianry search + arr sorted in asc
        # no target, search condition (min num) : use while l < r
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:  # Left side is sorted
                r = mid
            else:  # right side is sorted
                l = mid + 1
        return nums[l]  # either pointer is fine
