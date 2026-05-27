class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # initialize
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # 0 coins to make $0

        # build from $1 to target amount
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    # Current best vs. (1 current coin + optimal coins for remainder)
                    dp[a] = min(dp[a], 1 + dp[a - c])
        # if target is still palceholder value = impossible
        return dp[amount] if dp[amount] != amount + 1 else -1
