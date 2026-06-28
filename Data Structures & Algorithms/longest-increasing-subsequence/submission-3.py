class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # idea: keep track of prev num
        # can only proceed if cur > prev
        # pattern: 0 1 knapsack (either pick cur or skip cur)
        dp = {}

        def dfs(i, prev):
            # base case: out of bounds
            if i == len(nums):
                return 0
            # memo check
            if (i, prev) in dp:
                return dp[(i, prev)]

            skipCur = dfs(i + 1, prev)
            pickCur = 0
            if nums[i] > prev:
                pickCur = 1 + dfs(i + 1, nums[i])

            res = max(skipCur, pickCur)
            dp[(i, prev)] = res
            return res

        return dfs(0, float("-inf"))
