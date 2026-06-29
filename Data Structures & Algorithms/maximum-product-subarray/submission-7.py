class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # pattern: kadane btm up (L -> R)
        curMin, curMax = nums[0], nums[0]
        res = nums[0]

        for num in nums[1:]:
            curMin, curMax = (
                min(num, num * curMin, num * curMax),
                max(num, num * curMin, num * curMax),
            )
            # find max product
            res = max(res, curMax)
        return res
