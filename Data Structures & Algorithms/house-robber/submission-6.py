class Solution:
    def rob(self, nums: List[int]) -> int:
        # pattern: dp, keyword: max amount money
        # 01 knapsack (subproblem): rob cur or rob next
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 0  # rob 0 house = 0 profit
        dp[1] = nums[0]  # first house profit
        # L -> R (start from 1st)

        for i in range(2, n + 1):  # start from 2 bcs 0 and 1 base case already filled
            robCur = dp[i - 2] + nums[i - 1]  # skip 2 house bcs cannot rob adj
            robNext = dp[i - 1]
            dp[i] = max(robCur, robNext)

        return max(dp)
