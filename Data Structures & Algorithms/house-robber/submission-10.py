class Solution:
    def rob(self, nums: List[int]) -> int:
        # subproblem: rob cur or skip cur, find max money = dp
        # pattern: btm up approach, 0/1 knapsack
        # edge case: if no house or 1 house
        if not len(nums):
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # start from 2, until n
        for i in range(2, n):
            # after rob cur , need skip 2 house
            # dp is 1 indexed, nums is 0 indexed
            robCur = dp[i - 2] + nums[i]
            skipCur = dp[i - 1]
            dp[i] = max(robCur, skipCur)

        return dp[n - 1]
