class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort arr is first step
        nums.sort()
        res = []
        pair = []

        def backtrack(i):
            # base case
            if i >= len(nums):
                res.append(pair.copy())
                return
            # include i
            pair.append(nums[i])
            backtrack(i + 1)

            pair.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)
        
        backtrack(0)
        return res
