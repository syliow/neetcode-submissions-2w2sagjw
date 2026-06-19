class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # pattern: backtracking -> list all unique combinations
        res = []
        pair = []

        def dfs(i, cur):
            if cur == target:
                res.append(pair.copy())
                return
            # base case: out of bounds
            if i >= len(nums) or cur > target:
                return

            # recursion
            # include or exclude current num
            pair.append(nums[i])
            dfs(i, cur + nums[i])
            pair.pop()
            dfs(i + 1, cur)

        dfs(0, 0)
        return res
