class Solution:
    def rob(self, nums: List[int]) -> int:
        # pattern: btm up (optimized)
        # use 2 value
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for i in range(len(nums)):
            # skip cur
            # plus current + skip 2
            tmp = max(rob1, nums[i] + rob2)
            rob2 = rob1
            rob1 = tmp
        return rob1
