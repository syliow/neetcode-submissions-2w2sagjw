class Solution:
    def rob(self, nums: List[int]) -> int:
        # pattern: btm up approach
        if len(nums) == 1:
            return nums[0]
        res1 = self.helper(nums[1:])  # skip first
        res2 = self.helper(nums[:-1])  # skip last
        return max(nums[0], res1, res2)

    def helper(self, nums: List[int]) -> int:
        skipPrev, robPrev = 0, 0
        for num in nums:
            # either rob this house + what we had before last house
            # or skip this house and keep max money from last house
            robCur = max(skipPrev + num, robPrev)

            skipPrev = robPrev
            robPrev = robCur
            
        return robPrev
