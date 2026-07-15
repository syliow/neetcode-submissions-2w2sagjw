class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # (i, hasBought)

        def dfs(i, hasBought):
            # base case: out of bounds
            if i == len(prices):
                return 0
            # memo check
            if (i, hasBought) in dp:
                return dp[(i, hasBought)]
            # recursion
            res = 0
            # decide buy/sell or skip
            if hasBought:
                # Sell or skip
                sell = dfs(i + 1, False) + prices[i]
                skip = dfs(i + 1, True)
                res = max(sell, skip)
            else:
                # buy or skip
                buy = dfs(i + 1, True) - prices[i]
                skip = dfs(i + 1, False)
                res = max(buy, skip)

            dp[(i, hasBought)] = res
            return res

        return dfs(0, False)
