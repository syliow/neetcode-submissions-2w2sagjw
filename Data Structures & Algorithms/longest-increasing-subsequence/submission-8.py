class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # pattern: btm up approach
        dp = [1] * len(nums)

        for i in range(len(nums)):
            # j = prev num
            for j in range(i):
                #J is always before i 
                if nums[j] < nums[i]:
                    # longest sbq
                    #dp[i] = best ans so far
                    #dp[j] + 1 = can we find a better ans
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
