class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #core idea: dfs, either we include or exclude a num
        res = [] #final
        subset = [] #current ongoing subset

        def dfs(i):
            #push to res if ongoing subset reaches chara limit
            if i >= len(nums):
                res.append(subset.copy())
                return
            #include num
            subset.append(nums[i])
            dfs(i + 1)
            #exclude num
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res