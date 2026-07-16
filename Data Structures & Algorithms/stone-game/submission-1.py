class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # top down
        # max stones
        # basically counting first player total val
        dp = {}  # (l, r)

        def dfs(l, r):
            # base case
            if l > r:
                return 0
            # memo check
            if (l, r) in dp:
                return dp[(l, r)]
            # if even = means its first player turn
            even = (r - l) % 2 == 0
            left = piles[l] if even else 0
            right = piles[r] if even else 0

            # recursion
            res = 0

            res = max(
                # take first
                dfs(l + 1, r) + left,
                # take last
                dfs(l, r - 1) + right,
            )
            dp[(l, r)] = res
            return res

        total = sum(piles)
        aliceScore = dfs(0, len(piles) - 1)
        return aliceScore > total - aliceScore
