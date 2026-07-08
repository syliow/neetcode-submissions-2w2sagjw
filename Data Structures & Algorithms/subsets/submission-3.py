class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        pair = []

        def dfs(i):
            if i == len(nums):
                res.append(pair.copy())
                return
            
            #backtrack
            pair.append(nums[i])
            dfs(i + 1)

            pair.pop()
            dfs(i + 1)
            
        dfs(0)
        return res 