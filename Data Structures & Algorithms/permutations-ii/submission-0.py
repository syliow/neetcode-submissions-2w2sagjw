class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # permutations: possible combo of num in diff sequence
        res = []
        pair = []
        visited = set()
        # sort to prevent dup
        nums.sort()

        def dfs():
            # base case
            if len(nums) == len(pair):
                res.append(pair.copy())
                return

            for i in range(len(nums)):
                # skip if index is used
                if i in visited:
                    continue

                # skip dup
                # skip if num is same as prev
                # not in visited
                if i > 0 and nums[i] == nums[i - 1] and (i - 1) not in visited:
                    continue

                pair.append(nums[i])
                visited.add(i)

                dfs()

                pair.pop()
                visited.remove(i)

        dfs()
        return res
