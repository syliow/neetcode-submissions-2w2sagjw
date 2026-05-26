class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case: if only 1 num
        if len(nums) == 1:
            return nums[0]

        # just call the helper twice
        # 1. skip first, run on entire arr
        # 2. include entire arr , skip last
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            # either we include or exclude current house
            # get the max val
            newRob = max(rob1 + num, rob2)

            # move pointer forward
            rob1 = rob2
            rob2 = newRob  # now rob2 will contain max amount at end arr

        return rob2
