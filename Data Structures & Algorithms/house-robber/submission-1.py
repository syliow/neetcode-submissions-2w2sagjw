class Solution:
    def rob(self, nums: List[int]) -> int:
        #pattern: top down recursion
        #idea: either rob current or skip current
        memo = [-1] * len(nums)

        def dfs(i):
            #base case: if out of bounds
            if i >= len(nums):
                return 0
            #if i != -1 , let it continue calculate
            if memo[i] != -1:
                return memo[i]
            
            #recursion time: skip current or rob current
            #if skip = dfs(i + 1), move to next house , gain 0
            #if rob = dfs(i + 2), gain nums[i] + rob next 2nd house
            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return memo[i]
        return dfs(0)