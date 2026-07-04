class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # pattern: dp . why? we need to find largest product, return single ele
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            #if x use tmp,  we will calculate with new vals
            tmpMax = curMax * num
            tmpMin = curMin * num
            #reset when cur is better than prev
            curMin = min(num, tmpMin, tmpMax)
            curMax = max(num, tmpMin, tmpMax)
            # find largest product
            res = max(res, curMin, curMax)

        return res
