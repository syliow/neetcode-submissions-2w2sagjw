class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # top down
        # max stones
        dp = {}  # (l, r)

        def dfs(l, r):
            # base case
            if l > r:
                return 0
            # memo check
            if (l, r) in dp:
                return dp[(l, r)]
            # recursion
            res = 0

            res = max(
                # take first
                dfs(l + 1, r) + piles[l],
                # take last
                dfs(l, r - 1) + piles[r],
            )
            dp[(l, r)] = res
            return res

        return True if dfs(0, len(piles) - 1) > 0 else False
