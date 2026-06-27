class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #pattern: btm up approach
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(
                dp[i - 1], #skip cur
                dp[i - 2] + nums[i] #rob cur
            )
        return dp[-1]
        rob1, rob2 = 0, 0
        for _ in range(len(nums)):
            cur = max(rob2 + nums[i], rob1)
            #move index forward
            rob1 = rob2
            rob2 = cur
        return rob2

