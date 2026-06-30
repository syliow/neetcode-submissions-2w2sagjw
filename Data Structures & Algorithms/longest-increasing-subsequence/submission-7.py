class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # pattern: 0 1 knapsack
        dp = {}

        def dfs(i, prevIndex):
            # base case: out of bounds
            if i == len(nums):
                return 0
            # memo check
            if (i, prevIndex) in dp:
                return dp[(i, prevIndex)]

            # recursion
            skipCur = dfs(i + 1, prevIndex)
            pickCur = 0
            if prevIndex == -1 or nums[i] > nums[prevIndex]:
                pickCur = 1 + dfs(i + 1, i)
            dp[(i, prevIndex)] = max(skipCur, pickCur)
            return dp[(i, prevIndex)]

        return dfs(0, -1)
