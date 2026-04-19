class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #core idea: same as combo sum 1, need handle dup
        #sort and skip over dup
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            #include num
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i]) #no dup!
            #exclude num
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1 #skip over dups
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res