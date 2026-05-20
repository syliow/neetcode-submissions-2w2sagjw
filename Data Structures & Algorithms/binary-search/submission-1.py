class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pattern: log n time, sorted in asc = BS
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # go larget
                l = mid + 1
            else:
                # go smaller
                r = mid - 1
        # fallback
        return -1
