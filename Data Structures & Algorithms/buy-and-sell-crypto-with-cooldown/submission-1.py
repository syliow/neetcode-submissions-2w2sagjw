class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # pattern: dfs recursion memoization
        dp = {}  # [i, buying (bool): maxProfit]

        def dfs(i, buying):
            # base case: out of bounds
            if i >= len(prices):
                return 0

            # check dp
            if (i, buying) in dp:
                return dp[(i, buying)]

            # recursion time: either buy or sell/ cooldown (do nthg)
            if buying:
                # swap buying to false to avoid deadloop
                buy = dfs(i + 1, False) - prices[i]  # minus buy cost to count profit
                cd = dfs(i + 1, buying)  # no need count profit
                dp[(i, buying)] = max(buy, cd)
            # sell time
            else:
                sell = dfs(i + 2, True) + prices[i]  # add prices to count profit
                cd = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, cd)
            return dp[(i, buying)]

        return dfs(0, True)
