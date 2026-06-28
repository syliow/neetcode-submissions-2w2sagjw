class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, isBuying):
            # base case: out of bounds
            if i >= len(prices):
                return 0
            # memo check
            if (i, isBuying) in dp:
                return dp[(i, isBuying)]
            # recursion
            if isBuying:
                buy = dfs(i + 1, False) - prices[i]
                skip = dfs(i + 1, True)
                res = max(buy, skip)
            else:
                sell = dfs(i + 2, True) + prices[i]
                skip = dfs(i + 1, False)
                res = max(sell, skip)
            
            dp[(i, isBuying)] = res
            return res

        return dfs(0, True)