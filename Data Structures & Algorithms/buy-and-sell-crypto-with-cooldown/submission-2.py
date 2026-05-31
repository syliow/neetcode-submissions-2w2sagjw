class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # pattern: dp, recursion topdown
        # idea: sell + 1d cd, can only own 1 coin = after buy must sell
        # goal: find MAX profit
        # subproblem: check profit vs maxProfit (for every chance)

        maxP = 0
        dp = {}

        def dfs(i, isBuying):
            # base case: i out of bounds
            if i >= len(prices):
                return 0

            # memo check
            if (i, isBuying) in dp:
                return dp[(i, isBuying)]

            # recursion
            # either buy or sell, if sell, move i + 2 for cd
            if isBuying:
                # buy = negative profit
                # cd
                buy = dfs(i + 1, False) - prices[i]
                cooldown = dfs(i + 1, True)
                dp[(i, isBuying)] = max(buy, cooldown)
              
            else:
                # sell vs skip
                sell = dfs(i + 2, True) + prices[i]
                #we already holding a stock, cant set isbuying = true unless we sell
                cooldown = dfs(i + 1, False)
                dp[(i, isBuying)] = max(sell, cooldown)
             
            return dp[(i, isBuying)]

        return dfs(0, True)
