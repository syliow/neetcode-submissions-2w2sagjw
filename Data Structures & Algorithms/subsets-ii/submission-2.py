class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # pattern: backtrack -> return all possible subset
        res = []
        pair = []
        nums.sort()

        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(pair.copy())
                return

            pair.append(nums[i])
            dfs(i + 1)

            pair.pop()
            # look forward
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return res
