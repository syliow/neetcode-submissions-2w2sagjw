class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # pattern: 2d dp -> we need to keep track of index and remaining
        # subproblem: add current sub or subtract current sum?

        dp = {}  # [index, remaining]

        def dfs(i, remaining):
            # base case: success case
            if i >= len(nums) and remaining == 0:
                return 1
            # base case: invalid case (out of bounds)
            if i >= len(nums) and remaining != 0:
                return 0

            # memo check
            if (i, remaining) in dp:
                return dp[(i, remaining)]

            # recursion: find total num of ways (+ -) to reach target
            # choose add current num or subtract current num
            res = 0
            res = (
                dfs(i + 1, remaining + nums[i])  # add num
                + dfs(i + 1, remaining - nums[i])  # subtract num
            )
            dp[(i, remaining)] = res
            return res

        return dfs(0, target)
