class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # cannot use duplicate
        res = []
        pair = []
        candidates.sort()

        def dfs(i, total):
            # total matches target
            if total == target:
                res.append(pair.copy())
                return
            # base case: out of bounds
            if i >= len(candidates) or total > target:
                return

            # backtracking
            pair.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            pair.pop()
            # skip dup (only after we included them)
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)

        dfs(0, 0)
        return res
