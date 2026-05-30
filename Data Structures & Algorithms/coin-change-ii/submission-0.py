class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # pattern: recursion dfs memoization
        memo = {}

        # a = current amount
        def dfs(i, a):
            # base case
            if a == amount:
                return 1

            if a > amount:
                return 0

            if i >= len(coins):
                return 0

            # check memo
            if (i, a) in memo:
                return memo[(i, a)]

            # recursion
            # its either we pick the coin or skip it
            #ways from path a + ways from path b
            memo[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return memo[(i, a)]

        return dfs(0, 0)
