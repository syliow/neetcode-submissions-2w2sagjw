class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        pair = []

        def backtrack(i, total):
            # base case
            if total == target:
                res.append(pair.copy())
                return
            # edge case:
            if i >= len(nums) or total > target:
                return

            # total should be diff for evey recursive call
            pair.append(nums[i])
            backtrack(i, total + nums[i])  # can reuse multiple times so we use i

            pair.pop()
            backtrack(i + 1, total)  # total remains same bcs we didnt add

        backtrack(0, 0)
        return res
