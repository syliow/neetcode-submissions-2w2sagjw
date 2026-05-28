class Solution:
    def rob(self, nums: List[int]) -> int:
        #pattern: btm up approach (L -> R) step by step
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 0 #0 house = $0
        dp[1] = nums[0] #1 house = value of first house

        for i in range(2, n + 1):
            #skip current: move to next
            #rob current: grab money(nums[i - 1]) and move to 2nd next
            #L -> R : must look backwards in history
            dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])
        return dp[-1]