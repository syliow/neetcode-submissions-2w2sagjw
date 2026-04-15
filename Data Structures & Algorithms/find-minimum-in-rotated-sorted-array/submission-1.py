class Solution:
    def findMin(self, nums: List[int]) -> int:
        #one part is sorted, other part contains min val
        #use BS to identify which side is sorted
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            #find out which part is sorted
            #if num on l < num on r, means its perfectly sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            #mid might be the smallest
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]: #search right
                l = mid + 1
            else:
                r = mid - 1
        return res