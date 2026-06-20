class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #pattern: return all possible = backtracking
        res = []
        pair = []

        def backtracking(i):
            #base case
            if i >= len(nums):
                res.append(pair.copy())
                return
            
            pair.append(nums[i])
            backtracking(i + 1)

            pair.pop()
            backtracking(i + 1)
        
        backtracking(0)
        return res