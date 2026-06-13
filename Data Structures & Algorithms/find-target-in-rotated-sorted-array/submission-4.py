class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pattern: log n time -> binary search
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # compare mid against r to find the "sorted" side
            # sorted on r
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[r]:
                # search R side: mid < target < r
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:    
                    r = mid - 1
            # sorted on l
            else:
                # search L side: l <= target < mid
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1