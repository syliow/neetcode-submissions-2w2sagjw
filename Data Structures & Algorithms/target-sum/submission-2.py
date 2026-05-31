class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # pattern: total of diff ways  = check all combo , dp
        # subproblem: add or subtract from total sum
        # thought process
        #         2
        #     +2      - 2
        #     4       0
        # +2  -2
        # 6   2

        dp = {}

        def dfs(i, total):
            # reach end of nums, check whether total == target (must be exact)
            if i == len(nums):
                return 1 if total == target else 0

            # memo check
            if (i, total) in dp:
                return dp[(i, total)]

            # recursion
            res = 0
            # either we add, or subtract
            res += dfs(i + 1, (total + nums[i])) + dfs(i + 1, (total - nums[i]))
            dp[(i, total)] = res
            return res

        return dfs(0, 0)
