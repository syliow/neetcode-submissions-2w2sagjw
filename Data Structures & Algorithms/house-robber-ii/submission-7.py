class Solution:
    def rob(self, nums: List[int]) -> int:
        # pattern: btm up approach (R -> L)
        # subproblem: either we skip first and rob rest or skip last and rob rest
        if len(nums) == 1:
            return nums[0]

        # skip first or skip last
        # skip first: [1:]
        # skip last: [:-1]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        n = len(nums)
        dp = [0] * (n + 1)
        dp[n] = 0  # 0 house
        dp[n - 1] = nums[n - 1] #2nd last house

        # R -> L
        # <------ cur prev1 prev2
        for i in reversed(range(n-1)):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])

        return dp[0]
