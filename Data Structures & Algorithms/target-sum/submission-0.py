class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # pattern: dfs recursion
        memo = {}  # [index, total] = num of ways

        def dfs(i, total):
            # base case
            if i == len(nums):
                return 1 if total == target else 0

            # memo check
            if (i, total) in memo:
                return memo[(i, total)]

            # recursion
            memo[(i, total)] = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            return memo[(i, total)]

        return dfs(0, 0)
