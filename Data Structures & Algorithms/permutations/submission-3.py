class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #permutations: possible combo of num in diff sequence
        res = []
        pair = []
        visited = set()

        def dfs():
            #base case
            if len(nums) == len(pair):
                res.append(pair.copy())
                return
            
            for num in nums:
                if num not in visited:
                    pair.append(num)
                    visited.add(num) #keep track of index instead of values

                    dfs()
                    pair.pop()
                    visited.remove(num)
        dfs()
        return res