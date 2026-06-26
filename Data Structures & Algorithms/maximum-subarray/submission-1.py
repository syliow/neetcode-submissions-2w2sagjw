class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # pattern: top down memoization
        dp = {}

        def dfs(i, started):
            if i == len(nums):
                return 0 if started else float("-inf")

            # memo check
            if (i, started) in dp:
                return dp[(i, started)]

            if started:
                res = max(0, nums[i] + dfs(i + 1, True))
            else:
                skipCurrent = dfs(i + 1, False)
                startCurrent = nums[i] + dfs(i + 1, True)
                res = max(skipCurrent, startCurrent)
            dp[(i, started)] = res
            return res

        return dfs(0, False)
