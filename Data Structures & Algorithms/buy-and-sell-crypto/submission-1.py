class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # core idea: sliding window
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            # only sell if r > l, otherwise skip it
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r  # move L to R

            # always move R forward
            r += 1
        return maxProfit
