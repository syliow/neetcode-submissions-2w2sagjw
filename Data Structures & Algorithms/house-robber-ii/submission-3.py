class Solution:
    def rob(self, nums: List[int]) -> int:
        # pattern: brute force (recursion) -> Top down approach
        memo1 = [-1] * len(nums)
        memo2 = [-1] * len(nums)

        # edge case: only 1 element
        if len(nums) == 1:
            return nums[0]

        def dfs(i, houses, memo):
            # base case: out of bounds
            if i >= len(houses):
                return 0
            if memo[i] != -1:
                return memo[i]

            # recursion: skip or rob
            memo[i] = max(dfs(i + 1, houses, memo), houses[i] + dfs(i + 2, houses, memo))
            return memo[i]

        # rob from first to 2nd last (exclude last)
        option1 = dfs(0, nums[:-1], memo1)
        # rob from 2nd to last (exclude first)
        option2 = dfs(0, nums[1:], memo2)

        return max(option1, option2)
