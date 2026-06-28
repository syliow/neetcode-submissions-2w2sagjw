class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)] # +2 for extra 1s

        #L and R opposite direction
        for l in range(n, 0, -1): # R -> L
            for r in range(l, n + 1):
                for i in range(l, r + 1):
                    #go thru LR first
                    coins = dp[l][i - 1] + dp[i + 1][r]
                    #go thru coins at i index
                    coins += nums[l - 1] * nums[i] * nums[r + 1]
                    dp[l][r] = max(dp[l][r], coins)
        return dp[1][n]
