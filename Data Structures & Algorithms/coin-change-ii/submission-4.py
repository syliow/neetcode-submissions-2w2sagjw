class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # unbounded knapsack (reuse unlimited times)
        # subproblem: reuse this item or skip to next
        dp = {}

        def dfs(i, remaining):
            res = 0
            # base case: reach the target amt
            if remaining == 0:
                return 1
            # base case: if remaining coin too large/ out of bounds
            if remaining < 0 or i == len(coins):
                return 0
            # memo check
            if (i, remaining) in dp:
                return dp[(i, remaining)]
            # recursion
            res += dfs(i, remaining - coins[i])  # reuse cur
            res += dfs(i + 1, remaining)  # skip next
            dp[(i, remaining)] = res
            return res

        return dfs(0, amount)
