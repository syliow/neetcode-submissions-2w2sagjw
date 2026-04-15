class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 3 4 5 1 2
        # 3 < 5 > 2

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]: #right is sorted, search left
                r = mid
            else:
                l = mid + 1
        return nums[l] #final l and r will point at same val
