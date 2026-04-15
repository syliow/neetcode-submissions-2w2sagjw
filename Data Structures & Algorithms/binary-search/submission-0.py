class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            if nums[mid] > target:
                #go smaller, r -1
                r = mid - 1
            elif nums[mid] < target:
                #go bigger, l + 1
                l = mid + 1
            else:
                return mid
        return -1 #if not avaialable