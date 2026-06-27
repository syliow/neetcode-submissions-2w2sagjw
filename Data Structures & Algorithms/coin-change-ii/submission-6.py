class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # pattern: btm up approach - Space optimized (R -> L)
        n = len(coins)
        prev = [0] * (amount + 1)
        prev[0] = 1

        # fill table backwards
        for i in range(n - 1, -1, -1):
            curr = [0] * (amount + 1)
            curr[0] = 1

            for a in range(1, amount + 1):
                curr[a] = prev[a]  # skip coin
                if a - coins[i] >= 0:
                    curr[a] += curr[a - coins[i]]  # use coin
            prev = curr
        return prev[amount]
