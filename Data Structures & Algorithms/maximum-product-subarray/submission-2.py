class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # pattern: kadane algo (btm up approach)
        # kadane scans from L -> R once
        # idea: find largest product (cannot skip number)

        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            curMin, curMax = (
                min(num, curMin * num, curMax * num),
                max(num, curMin * num, curMax * num),
            )
            res = max(res, curMax)
        return res
