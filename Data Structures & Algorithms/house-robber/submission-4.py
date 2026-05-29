class Solution:
    def rob(self, nums: List[int]) -> int:
        # pattern: btm up approach (dp for loop)
        # subproblem: rob current house or skip current and rob 2 house after
        n = len(nums)
        # edge case
        if n == 1:
            return nums[0]

        dp = [0] * (n + 1)

        dp[0] = 0  # rob 0 house = $ 0
        dp[1] = nums[0]  # if only rob 1 house, we get 1st house val

        # start at 2
        for i in range(2, n + 1):
            # either we rob or skip, get highest val
            dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])

        return dp[n]
