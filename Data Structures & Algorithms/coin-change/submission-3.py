class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #pattern: btm up approach (R -> L)
        #subproblem: which min amount of coin can i pick next to make up target amount
        #early return
        if amount == 0:
            return 0
        #[0, 1, 2, 3, 4, 5...]
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
              if i - c >= 0:
                #Pick the current coin + look back at the remainder
                dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if dp[amount] != float("inf") else -1