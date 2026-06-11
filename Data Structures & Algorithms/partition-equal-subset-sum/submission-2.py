class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # pattern: 2D DP (top down memoization)
        # either we include the num or exlude it
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2  # both side must be equal

        dp = {}  # i, curTarget

        def dfs(i, remaining):
            # if we reach the target
            if remaining == 0:
                return True

            # base case: out of bounds or over
            if i >= len(nums) or remaining < 0:
                return False

            # memo check
            if (i, remaining) in dp:
                return dp[(i, remaining)]

            # recursion: include cur or skip cur
            dp[(i, remaining)] = dfs(i + 1, remaining - nums[i]) or dfs(i + 1, remaining)
            return dp[(i, remaining)]

        return dfs(0, target)
