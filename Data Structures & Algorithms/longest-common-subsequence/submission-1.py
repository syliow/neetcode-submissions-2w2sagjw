class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #pattern: 2d dp, recursion
        #idea: compare 2 string, allowed to "skip" charas
        #subproblem: do we delete this char? do we keep this char? when do we move i and j?

        dp = {}

        #compare i vs j
        #only move i when text1[i] == text2[j]
        def dfs(i, j):
            #base case: check either pointer runs out of chara
            if i >= len(text1):
                return 0
            if j >= len(text2):
                return 0

            #memo check
            if (i, j) in dp:
                return dp[(i, j)]

            #recursion
            res = 0
            if text1[i] == text2[j]:
                #move both pointer forward
                #remember to plus one
                res +=  1 + dfs(i + 1, j + 1)
            else:
                #either we skip i or j
                res += max(dfs(i, j + 1), dfs(i + 1, j))
            dp[(i, j)] = res
            return res
        
        return dfs(0, 0)
            

