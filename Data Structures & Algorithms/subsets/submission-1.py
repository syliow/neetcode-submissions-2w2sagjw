class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # core idea: include or exclude
        res = []
        pair = []

        def backtrack(i):
            # base case
            if i >= len(nums):
                res.append(pair.copy())
                return

            # include or exclude nums i in pairs
            pair.append(nums[i])
            backtrack(i + 1)

            pair.pop()
            backtrack(i + 1)

        backtrack(0)
        return res
