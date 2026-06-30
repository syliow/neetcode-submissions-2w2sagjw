class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # pattern: top down approach
        dp = {}

        def dfs(i, remaining):
            # base case
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            #base case: out of bounds
            if i == len(coins):
                return 0

            # memo check
            if (i, remaining) in dp:
                return dp[(i, remaining)]
            res = 0
            #reuse coin or skip coin
            reuse = dfs(i, remaining - coins[i])
            skip = dfs(i + 1, remaining)
            res = reuse + skip

            dp[(i, remaining)] = res
            return res

        return dfs(0, amount)
