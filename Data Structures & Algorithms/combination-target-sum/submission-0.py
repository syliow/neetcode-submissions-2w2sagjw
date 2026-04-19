class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #core idea: include the num or exclude it
        res = []

        #cur = current combo
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            #out of bounds
            if i >= len(nums) or total > target:
                return
            #include num
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            #exclude num
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res