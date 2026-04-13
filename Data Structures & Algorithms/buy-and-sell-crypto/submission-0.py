class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        #r must be > than l in order to sell
        #otherwise move l to r
        while r < len(prices):
            #we sell (profit)
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max (maxProfit, profit)
            else:
                l = r
            #always move r
            r += 1
        return maxProfit
            