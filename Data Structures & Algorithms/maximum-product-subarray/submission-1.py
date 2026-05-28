class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # pattern: brute force -> top down (recursion)
        # problem: find subarray that has largest product
        # subproblem: find min and max at index i

        res = nums[0]
        # Brute force only: literally keep multiply by right
        for i in range(len(nums)):
            cur = nums[i]
            res = max(res, cur)

            for j in range(i + 1, len(nums)):
                cur *= nums[j]
                res = max(res, cur)
        return res
