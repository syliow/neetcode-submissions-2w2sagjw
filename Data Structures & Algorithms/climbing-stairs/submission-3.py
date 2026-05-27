class Solution:
    def climbStairs(self, n: int) -> int:
        #brute force: dfs
        # def dfs(i):
        #     #base case
        #     if i >= n:
        #         return i == n
            
        #     #recursion: sum of both choices
        #     #issue 1: repeating subproblems
        #     #solution 1: store result after compute, reuse it (caching)
        #     # return dfs(i + 1) + dfs(i + 2)
        # return dfs(0)

        #Top down approach (recursion)
        #-1 is placeholder
        dp = [-1] * n

        def dfs(i):
            #base case
            if i >= n:
                return i == n
            #if == -1, means we havent calculate yet
            if dp[i] != -1:
                return dp[i]
            dp[i] = dfs(i + 1) + dfs(i + 2)
            return dp[i]
        
        return dfs(0)

