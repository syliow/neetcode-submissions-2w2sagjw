class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # pattern: find total possible combos
        # unlimited num = can reuse
        # unbounded knapsack: reuse cur or skip to next
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1  # base case

        for coin in coins:
            for i in range(coin, amount + 1):  # stop before amount
                # if i use cur coin, the reamining = i - coin
                dp[i] += dp[i - coin]
        return dp[amount]
