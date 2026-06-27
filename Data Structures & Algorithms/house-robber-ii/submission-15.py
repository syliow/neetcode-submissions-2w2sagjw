class Solution:
    def rob(self, nums: List[int]) -> int:
        # pattern: btm up approach
        #skip first or skip last
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        skipPrev, robPrev = 0, 0
        for num in nums:
            # either rob this house + what we had before last house
            # or skip this house and keep max money from last house
            robCur = max(skipPrev + num, robPrev)

            skipPrev = robPrev
            robPrev = robCur

        return robPrev
