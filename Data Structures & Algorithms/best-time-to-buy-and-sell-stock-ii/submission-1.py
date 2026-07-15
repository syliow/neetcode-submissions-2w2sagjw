class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # pattern: btm up approach
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        # from R -> L
        for i in range(n - 1, -1, -1):
            # dp[X][0] = hasBought False
            # dp[X][1] = hasBought True
            buy = dp[i + 1][1] - prices[i]
            skip = dp[i + 1][0]
            dp[i][0] = max(buy, skip)

            sell = dp[i + 1][0] + prices[i]
            skip = dp[i + 1][1]
            dp[i][1] = max(sell, skip)

        return dp[0][0]
