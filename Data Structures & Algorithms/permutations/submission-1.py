class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #core idea, use set to keep track of visited
        visited = set()
        res = []
        pair = []

        def backtrack():
            #base case
            #pair is full and used up all num in nums
            if len(pair) >= len(nums):
                res.append(pair.copy())
                return

            for num in nums:
                if num not in visited:
                    pair.append(num)
                    visited.add(num)

                    #recursion
                    backtrack()

                    #exclude num
                    pair.pop()
                    visited.remove(num)

        backtrack()
        return res
