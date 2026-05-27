class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * num
            # passing in num for edge case: 0
            # 0 * anything = 0
            # to "reset" it, we can set it to num isntead
            curMax = max(curMax * num, curMin * num, num)
            # use tmp to avoid use latest curmax
            curMin = min(tmp, curMin * num, num)
            # compare against res for largest product
            res = max(res, curMax)

        return res
