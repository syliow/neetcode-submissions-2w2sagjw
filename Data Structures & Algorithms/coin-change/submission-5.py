class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # pattern: 1d dp, top down memoization
        dp = [-1] * (amount + 1)

        def dfs(amount):
            # base case
            if amount == 0:
                return 0
            # memo check
            if dp[amount] != -1:
                return dp[amount]
            # recursion
            res = float("inf")
            for coin in coins:
                if amount - coin >= 0:
                    # + 1 for current coin picked
                    res = min(res, 1 + dfs(amount - coin))
            dp[amount] = res
            return res

        mincoins = dfs(amount)
        return mincoins if mincoins != float("inf") else -1
