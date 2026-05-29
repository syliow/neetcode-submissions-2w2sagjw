class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # pattern: top down approach (memoization)
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0

            # memo check
            if amount in memo:
                return memo[amount]

            # recursion
            res = float("inf")
            for coin in coins:
                # means we can continue dfs
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            memo[amount] = res
            return res

        ans = dfs(amount)
        return ans if ans != float("inf") else -1
