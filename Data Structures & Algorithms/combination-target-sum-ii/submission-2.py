class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        pair = []
        candidates.sort()

        def backtrack(i, total):
            # base case
            if total == target:
                res.append(pair.copy())
                return

            # edge case
            if total > target or i >= len(candidates):
                return

            pair.append(candidates[i])
            backtrack(i + 1, total + candidates[i])

            pair.pop()
            # skip dup only when we decide to exclude a num
            # include cannot skip dup bcs we might still need it
            # we exclude dup from excluding to avoid subset duplicate
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, total)

        backtrack(0, 0)
        return res
