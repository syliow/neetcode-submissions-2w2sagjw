class Solution:
    def rob(self, nums: List[int]) -> int:
        # pattern: btm up approach (L -> R)
        # compute from smallest to largest, step by step
        if len(nums) == 1:
            return nums[0]
        # exclude first house
        # exclude last house
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 0  # 0 house = $0
        dp[1] = nums[0]

        for i in range(2, n + 1):
            # skip first house or skip last house
            dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])

        return dp[-1]
