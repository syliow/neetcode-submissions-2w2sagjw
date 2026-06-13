class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # pattern: return all permutations = backtracking
        pair = []
        res = []
        visited = set()  # to keep track of used num

        def dfs():
            # base case: gone thru all num
            if len(pair) == len(nums):
                res.append(pair.copy())
                return
            # use a for loop instead
            # to loop through all num
            for num in nums:
                # backtracking
                if num not in visited:
                    pair.append(num)
                    visited.add(num)

                    # recurse to find the next number
                    dfs()
                    # undo choice
                    pair.pop()
                    visited.remove(num)  # use the num again for other pair

        dfs()
        return res
