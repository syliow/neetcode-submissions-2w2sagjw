class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # pattern: unbounded knapsack (top down memoization)
        # include 0 too
        dp = [-1] * (amount + 1)
        dp[0] = 0

        def dfs(remaining):
            # base case: if amount = 0, found match
            if remaining == 0:
                return 0
            # base case: amount too large
            if remaining < 0:
                return float("inf")
            # memo check
            if dp[remaining] != -1:
                return dp[remaining]

            # subproblem: use coin again / skip
            res = float("inf")
            for c in coins:
                # check valid
                res = min(res, 1 + dfs(remaining - c))

            dp[remaining] = res
            return res

        res = dfs(amount)
        return res if res != float("inf") else -1