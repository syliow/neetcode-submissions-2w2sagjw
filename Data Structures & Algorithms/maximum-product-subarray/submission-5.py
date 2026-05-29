class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # pattern: btm up (kadane) L -> R
        # idea: pass in both curMax and curMin
        # min * min could be huge positive

        curMin, curMax = nums[0], nums[0]
        res = nums[0]

        for num in nums[1:]:
            curMin, curMax = (
                min(num, num * curMin, num * curMax),
                max(num, num * curMin, num * curMax),
            )
            res = max(res, curMax)
        return res
