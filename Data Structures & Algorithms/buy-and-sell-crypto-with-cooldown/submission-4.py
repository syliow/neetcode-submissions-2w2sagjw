class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # pattern: DP -> return max profit so we need calculate all possible combo
        # subproblem: after buy, either sell coin or skip to next day
        # after sell, skip 2 days, if no sell, skip 1 day
        # 2d dp: track [(index, hasBought)]

        # top down memoization
        dp = {}

        def dfs(i, hasBought):
            # base case: out of bounds
            if i >= len(prices):
                return 0
            # memo check
            if (i, hasBought) in dp:
                return dp[(i, hasBought)]
            # recursion
            # if no coin, buy today or skip buy today
            if not hasBought:
                dp[(i, hasBought)] = max(
                    dfs(i + 1, True) - prices[i],  # buy today
                    dfs(i + 1, False),  # skip buy
                )
            # sell or no sell
            else:
                dp[(i, hasBought)] = max(
                    dfs(i + 2, not hasBought) + prices[i],  # sell
                    dfs(i + 1, hasBought),  # no sell so no profit, still own coin
                )
            return dp[(i, hasBought)]

        return dfs(0, False)
