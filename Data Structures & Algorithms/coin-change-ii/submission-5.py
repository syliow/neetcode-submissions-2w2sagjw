class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # pattern: btm up approach (R -> L)
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        coins.sort()  # prevent dups

        # base case: 1 way to use 0 amount: use no coins
        for i in range(n + 1):
            dp[i][0] = 1

        # fill table backwards
        for i in range(n - 1, -1, -1):
            for a in range(1, amount + 1):
                # option 1: skip cur
                dp[i][a] = dp[i + 1][a]
                # option 2: use cur
                if a - coins[i] >= 0:
                    dp[i][a] += dp[i][a - coins[i]]
        return dp[0][amount]
