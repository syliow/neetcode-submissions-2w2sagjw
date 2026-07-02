class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # pattern: dp top down memo
        # not backtracking bcs we not undo and go back
        # 2d dp = (i, remaining)
        dp = {}

        def dfs(i, total):
            # base case: remaining = target
            if i == len(nums):
                return 1 if total == target else 0

            # memo check
            if (i, total) in dp:
                return dp[(i, total)]
            # recursion
            res = 0
            res += dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            dp[(i, total)] = res
            return res

        return dfs(0, 0)
