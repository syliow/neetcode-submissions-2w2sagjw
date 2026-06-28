class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # pattern: btm up approach
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                # i is always on L , j is always on R
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
