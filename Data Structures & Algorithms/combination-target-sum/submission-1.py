class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #core idea: backtracking
        #include or exclude num
        res = []
        
        def dfs(i, cur, total):
            #matching
            if total == target:
                res.append(cur.copy())
                return

            #out of bounds
            if i >= len(nums) or total > target:
                return

            #include and exclude num
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res

