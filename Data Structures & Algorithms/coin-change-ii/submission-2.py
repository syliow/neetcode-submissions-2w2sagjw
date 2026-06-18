class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # pattern: dp, top down memoization
        # unbounded knapsack
        # subproblem: reuse the coin again or skip to next coin
        # 2d dp bcs we need to track {i, remaining}
        dp = {}

        def dfs(i, amount):
            # base case: success case
            if amount == 0:
                return 1  # count as a way
            # base case: invalid case
            if amount < 0 or i == len(coins):
                return 0

            # memo check
            if (i, amount) in dp:
                return dp[(i, amount)]
            # recursion: use this item again or skip to next
            res = 0
            for coin in coins:
                reuseCoin = dfs(i, amount - coins[i])
                skipCoin = dfs(i + 1, amount)
                res = reuseCoin + skipCoin  # find total combo
            dp[(i, amount)] = res
            return res

        return dfs(0, amount)
