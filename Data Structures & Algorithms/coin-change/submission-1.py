class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # pattern: brute force -> Top down approach
        # problem: how many num of coins we need to == amount
        # subproblem: after we take X coin, how much more we need for amount

        # pick one coin, remaining = amount - coin val
        # pick min coin combo
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            
            #memo check
            if amount in memo:
                return memo[amount]
                
            res = float("inf")
            for coin in coins:
                # we want to avoid using coin with over value
                if amount - coin >= 0:
                    # recursion
                    #make sure to include current coin too
                    res = min(res, 1 + dfs(amount - coin))
            memo[amount] = res
            return res

        minCoins = dfs(amount)
        return minCoins if minCoins != float("inf") else -1
