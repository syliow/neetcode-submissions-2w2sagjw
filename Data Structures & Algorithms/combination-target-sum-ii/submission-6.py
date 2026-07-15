class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # pattern: backtracking, retutrn all combinations, no dup , sort
        candidates.sort()
        res = []
        pair = []

        def dfs(i, total):
            # base case
            if total == target:
                res.append(pair.copy())
                return
            # base case: out of bounds or total exceeded
            if i == len(candidates) or total > target:
                return

            pair.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            pair.pop()
            # handle dup
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, total)

        dfs(0, 0)
        return res