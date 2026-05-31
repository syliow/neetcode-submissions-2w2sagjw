class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # pattern: dfs recursion top down
        # idea: find the total possible combo that makes up amount
        # subproblem: include current coin or skip curr ?

        memo = []
        for _ in range(len(coins) + 1):
            memo.append([-1] * (amount + 1))

        def dfs(i, a):
            # base case: a == amount
            if a == 0:
                return 1
            # if over 0
            if a < 0:
                return 0

            # out of bounds
            if i >= len(coins):
                return 0

            # memo check
            if memo[i][a] != -1:
                return memo[i][a]

            # recursion check
            # skip or add coins (count possible combo, no num of coins so dunnid +1 here)
            memo[i][a] = dfs(i + 1, a) + dfs(i, a - coins[i])
            return memo[i][a]

        return dfs(0, amount)
