class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # pattern: unique combinations : return all combinations
        # Backtracking
        res = []
        pair = []

        def backtracking(i, sum):
            # base case: reach target
            if sum == target:
                res.append(pair.copy())
                return
            #base case
            if sum > target:
                return
            
            # base case: out of bounds
            if i == len(nums):
                return
            # backtrack
            pair.append(nums[i])
            #use curr num
            backtracking(i, sum + nums[i])

            pair.pop()
            #use next num
            backtracking(i + 1, sum)

        backtracking(0, 0)
        return res
