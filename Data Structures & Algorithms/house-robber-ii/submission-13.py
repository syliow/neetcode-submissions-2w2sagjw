class Solution:
    def rob(self, nums: List[int]) -> int:
        # pattern: btm up approach
        if len(nums) == 1:
            return nums[0]
        res1 = self.helper(nums[1:])  # skip first
        res2 = self.helper(nums[:-1])  # skip last
        return max(res1, res2)

    def helper(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(
                dp[i - 2] + nums[i],  # rob cur
                dp[i - 1],  # skip cur
            )

        return dp[-1]
