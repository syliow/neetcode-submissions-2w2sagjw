class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # pattern: btm up (L -> R)
        dp = [float("inf")] * (amount+ 1)
        dp[0] = 0

        # start from 1 until amount, we try all combo
        for curAmount in range(1, amount + 1):
            for coin in coins:
                if curAmount - coin >= 0:
                    dp[curAmount] = min(dp[curAmount], 1 + dp[curAmount - coin])

        return dp[amount] if dp[amount] != float("inf") else -1
