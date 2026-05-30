class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # pattern: btm up approach (R -> L)
        # why r -> L ? bcs might right index can only have 1 sequence
        # we expand towards left side

        n = len(nums)
        dp = [1] * n

        for i in range(n - 1, -1, -1):
            # we can only form a sequence if i < j
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    # Compare current best at i vs jumping to j
                    dp[i] = max(dp[i], 1 + dp[j]) 

        return max(dp)
