class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        # buy must be < sell
        l = 0
        for r in range(len(prices)):
            # only buy if buy price < sell price
            if prices[r] > prices[l]:
                # good day to buy, but not best day
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                # if didnt found a good day, we move l
                l = r
        return maxProfit
